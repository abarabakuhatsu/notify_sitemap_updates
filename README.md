# Notify Sitemap Updates

GtihubActions を使ってサイトマップを定期的にチェックして、更新があった場合はグーグルに通知する。

## 設定用環境変数

SITEMAP_URL: 更新確認するサイトマップの完全な URL。**必須**。  
/sitemap/sitemap-0.xml のように実際に内容が更新される sitemap を登録する。

SITEMAP_INDEX_URL: 更新が確認されると Google へ通知する URL。  
設定されていない場合は SITEMAP_URL を送信する。  
gatsby-plugin-sitemap 4 以降では自動生成される /sitemap/sitemap-index.xml を登録する。
