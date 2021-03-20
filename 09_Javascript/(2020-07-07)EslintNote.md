Eslint Note
===

## VSCode で使う

```bash
npm install -g eslint
npm run lint
```

TypeScript で使いたいときは

```json
"eslint.validate": [
    "javascript",
    "typescript",
]
```


## Sample code

このノートを設けたのは、このコメントを参照することが多いため。

```JavaScript
// eslint-disable-next-line @typescript-eslint/no-var-requires
// eslint-disable-line @typescript-eslint/no-var-requires
// eslint-disable-line @typescript-eslint/no-unused-vars
/* eslint-disable */
// eslint-disable-next-line no-console
```
