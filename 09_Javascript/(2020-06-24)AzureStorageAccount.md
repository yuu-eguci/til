Azure Storage Account Note
===

## Installation

```bash
install --save @azure/storage-blob
```

## Sample code

sails.js を使っています。

```JavaScript
const { BlobServiceClient, StorageSharedKeyCredential } = require('@azure/storage-blob');

// 環境変数から StorageAccountName, AccessKey を取得します。
const account = sails.config.custom.azureStorageAccountName;
const accountKey = sails.config.custom.azureStorageAccountAccessKey;

// StorageAccount クライアントを作ります。
const sharedKeyCredential = new StorageSharedKeyCredential(account, accountKey);
const blobServiceClient = new BlobServiceClient(
  `https://${account}.blob.core.windows.net`,
  sharedKeyCredential
);

// コンテナクライアントを作ります。
// コンテナ名に xxxx/yyyy こういう指定はできない。 Storage は1階層らしい。
const containerClient = blobServiceClient.getContainerClient(`newcontainer${new Date().getTime()}`);

// コンテナを作ります。
// Storage Account > Blob service > Containers から閲覧できるフォルダがいっこ増えます。
const createContainerResponse = await containerClient.create();
console.info({ createContainerResponse });
// こんなのが取得できました。
// { createContainerResponse: 
//    { etag: '"0x8D817FA83D07E76"',
//      lastModified: 2020-06-24T04:53:19.000Z,
//      clientRequestId: '1af28305-b36b-4a4e-a3cf-e1306489895f',
//      requestId: '0c630c6c-101e-0013-20e3-49b5d2000000',
//      version: '2019-07-07',
//      date: 2020-06-24T04:53:18.000Z,
//      errorCode: undefined,
//      'content-length': '0',
//      server: 'Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0',
//      body: undefined } }

// コンテナの一覧を取得します。
// このあたりは @azure/storage-blob のドキュメント通り。
// https://www.npmjs.com/package/@azure/storage-blob
const iter = blobServiceClient.listContainers();
const containerNames = [];
let containerItem = await iter.next();
while (!containerItem.done) {
  console.info({ 'containerItem.value.name': containerItem.value.name });
  // こんなのが取得できました。
  // { 'containerItem.value.name': 'newcontainer1592975625139' }
  containerNames.push(containerItem.value.name);
  containerItem = await iter.next();
}

const content = 'Hello world!';
const blobName = 'newblob' + new Date().getTime();
const blockBlobClient = containerClient.getBlockBlobClient(blobName);
const uploadBlobResponse = await blockBlobClient.upload(content, content.length);
console.info({ uploadBlobResponse });
// { uploadBlobResponse: 
//    { etag: '"0x8D817FF1231B51E"',
//      lastModified: 2020-06-24T05:25:56.000Z,
//      contentMD5: <Buffer 86 fb 26 9d 19 0d 2c 85 f6 e0 46 8c ec a4 2a 20>,
//      clientRequestId: 'b22868b6-b51e-4f03-9ad2-c0658ad4e6d4',
//      requestId: 'd17be6f4-901e-002b-4ee7-49f48b000000',
//      version: '2019-07-07',
//      date: 2020-06-24T05:25:55.000Z,
//      isServerEncrypted: true,
//      encryptionKeySha256: undefined,
//      encryptionScope: undefined,
//      errorCode: undefined,
//      'content-length': '0',
//      server: 'Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0',
//      'x-ms-content-crc64': '3A5LeOL3NEk=',
//      body: undefined } }

// コンテナ内の blob 一覧を取得。
const iter2 = containerClientByName.listBlobsFlat();

const blobNames = [];
let blobItem = await iter2.next();
while (!blobItem.done) {
  console.info({ 'blobItem.value.name': blobItem.value.name });
  blobNames.push(blobItem.value.name);
  blobItem = await iter2.next();
}
```

## ContainerClient を取得する

`ContainerClient` のプロパティとかメソッドは公式ドキュメントを。

- https://docs.microsoft.com/en-us/javascript/api/@azure/storage-blob/containerclient?view=azure-node-latest

```JavaScript
// Storage Account を利用するためのライブラリです。
const { ContainerClient, StorageSharedKeyCredential, RestError } = require('@azure/storage-blob');

// Storage Account 接続用の設定です。
const storageAccountName = sails.config.custom.azureStorageAccountName;
const accessKey = sails.config.custom.azureStorageAccountAccessKey;

// Use StorageSharedKeyCredential with storage account and account key.
const sharedKeyCredential = new StorageSharedKeyCredential(storageAccountName, accessKey);

// コンテナクライアントを生成します。
// NOTE: BlobServiceClient から作るサンプルコードもありますが、このように直接 ContainerClient を生成することもできます。
const containerClient = new ContainerClient(`https://${storageAccountName}.blob.core.windows.net/${inputs.containerName}`, sharedKeyCredential);

// 実際にコンテナを create します。
// すでに存在する場合は RestError, ContainerAlreadyExists が発生します。正常な動きなのでスルーとなります。
try {
  await containerClient.create();
} catch (err) {
  // すでに存在する場合は RestError, ContainerAlreadyExists が発生しますが、2度目以降のアクセスでは正常です。
  if (err instanceof RestError && err.details.errorCode === 'ContainerAlreadyExists') {
  }
}
```

## すでに存在する container をもう一度 create しようとしたら?

RestError 出ます。

```
{ err: RestError: ﻿<?xml version="1.0" encoding="utf-8"?><Error><Code>ContainerAlreadyExists</Code><Message>The specified container already exists.
RequestId:2369c3b8-401e-000b-34ef-499847000000
Time:2020-06-24T06:17:56.4740092Z</Message></Error> 
 {
  "name": "RestError",
  "statusCode": 409,
  "request": {
    "streamResponseBody": false,
    "url": "https://taskaltimecardstoragestg.blob.core.windows.net/xxxx?restype=REDACTED",
    "method": "PUT",
    "headers": {
      "_headersMap": {
        "x-ms-version": "REDACTED",
        "user-agent": "azsdk-js-storageblob/12.1.2 (NODE-VERSION v8.9.4; Linux 4.19.76-linuxkit)",
        "x-ms-client-request-id": "09d45576-dc4e-41b9-a1ec-46a23442f6ee",
        "x-ms-date": "REDACTED",
        "authorization": "REDACTED",
        "cookie": "REDACTED"
      }
    },
    "withCredentials": false,
    "timeout": 0,
    "keepAlive": true,
    "decompressResponse": false,
    "requestId": "09d45576-dc4e-41b9-a1ec-46a23442f6ee"
  },
  "details": {
    "clientRequestId": "09d45576-dc4e-41b9-a1ec-46a23442f6ee",
    "requestId": "2369c3b8-401e-000b-34ef-499847000000",
    "version": "2019-07-07",
    "date": "2020-06-24T06:17:55.000Z",
    "errorCode": "ContainerAlreadyExists",
    "content-length": "230",
    "content-type": "application/xml",
    "server": "Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0",
    "message": "The specified container already exists.\nRequestId:2369c3b8-401e-000b-34ef-499847000000\nTime:2020-06-24T06:17:56.4740092Z",
    "Code": "ContainerAlreadyExists"
  },
  "message": "﻿<?xml version=\"1.0\" encoding=\"utf-8\"?><Error><Code>ContainerAlreadyExists</Code><Message>The specified container already exists.\nRequestId:2369c3b8-401e-000b-34ef-499847000000\nTime:2020-06-24T06:17:56.4740092Z</Message></Error>"
} }
```
