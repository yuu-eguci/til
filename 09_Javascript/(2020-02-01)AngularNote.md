AngularNote
===

- [ドキュメント](https://angular.jp/docs)

## angular-cli

```bash
# angular-cli 入ってたっけ?
npm ls --depth=0 -g

# angular-cli インストール。
npm install -g @angular/cli@latest

# プロジェクト作成。
ng new PROJECT --style=sass

# Would you like to add Angular routing? (y/N)
# SPA 使うか? ってこと。

# WARN の解決。 dev にしたほうがいいとかある?
npm install --save core-js@^3 jasmine-core@^3.5

# angular-cli-ghpages 追加。
ng add angular-cli-ghpages

# コンポーネント追加。
ng generate component COMPONENT
```

## Version

```bash
ng version
```

こういうのが見れる。

```plaintext
Angular CLI: 8.3.23
Node: 12.13.1
OS: darwin x64
Angular: 8.2.14
... animations, common, compiler, compiler-cli, core, forms
... language-service, platform-browser, platform-browser-dynamic
... router
```

## 構造ディレクティブ

```html
<div *ngFor="let i of this.x; let index=index; let first=first; let last=last; let even=even; let odd=odd"></div>

<a *ngIf="this.x" class="btn post-category"></a>
```