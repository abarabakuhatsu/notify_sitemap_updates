# Notify Sitemap Updates

GtihubActions を使ってサイトマップを定期的にチェックして、更新があった場合はグーグルに通知する。  
gatsby と gatsby-plugin-sitemap で生成されたサイトへの利用を想定して制作。

## actions の設定例

```yml
- name: Setup Python
  uses: actions/setup-python@v2
  with:
    python-version: '3.9'
    architecture: 'x64'

- name: Run notify sitemap updates
  run: python notify_sitemap_updates.py
  env:
    SITEMAP_URL: 'https://foo.com/sitemap/sitemap-0.xml'
    SITEMAP_INDEX_URL: 'https://foo.com/sitemap/sitemap-index.xml'
```

## 設定用環境変数

SITEMAP_URL: 更新確認するサイトマップの完全な URL。**必須**。  
`https://foo.com/sitemap/sitemap-0.xml` のように実際に内容が更新される sitemap を登録する。

SITEMAP_INDEX_URL: 更新が確認されると Google へ通知する URL。  
gatsby-plugin-sitemap 4 以降では自動生成される `https://foo.com/sitemap/sitemap-index.xml` を登録するイメージ。  
設定されていない場合は SITEMAP_URL を送信する。
