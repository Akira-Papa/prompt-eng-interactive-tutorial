# Anthropicのプロンプトエンジニアリング・インタラクティブチュートリアル

Anthropicのインタラクティブなプロンプトエンジニアリングチュートリアルへようこそ！このチュートリアルでは、モデルプロバイダーを問わず使えるプロンプティングの基礎を学習します。

<br>

<img src="./assets/header.png" alt="Anthropic Logo" width="600">

---

## 🎯 **対象者は？**
このチュートリアルは、経験レベルに関係なく**現代のプロンプティング技術**を学びたい方を対象としています。AIが初めての方でも、経験豊富な開発者でも、言語モデルからより良い結果を得るのに役立つ実践的な技術を発見できます。

<br>

## 🧠 **何を学べるの？**
### **中核となる基礎:**
- 効果的なプロンプトの構造化方法
- 明確性と精度のベストプラクティス
- AIとの安全で責任ある作業

### **高度な技術:**
- ロールプロンプティングとペルソナ割り当て
- 例を使ったFew-Shotプロンプティング
- 思考連鎖推論
- プロンプトチェーンと複雑なワークフロー
- ツール使用と関数呼び出し
- 幻覚の軽減

<br>

## 🎓 **チュートリアル構成**

このチュートリアルには**実践的なGoogle Sheetsバージョン**と**Jupyterノートブック**が含まれています。最適な方法を選択してください！

### **📊 Google Sheets（初心者向けお勧め）**
入門に最適 - コーディング不要！
- **[Google Sheetsチュートリアルはこちら →](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weOuttqDhiTCVcgA/edit?usp=sharing)**

### **📓 Jupyter Notebooks（開発者向け）**
3つの異なるバージョンが利用可能：

1. **[Anthropic 1P/](./Anthropic%201P/)** - 直接Anthropic API
2. **[AmazonBedrock/anthropic/](./AmazonBedrock/anthropic/)** - Bedrock経由のAnthropic SDK
3. **[AmazonBedrock/boto3/](./AmazonBedrock/boto3/)** - Bedrockでのboto3

<br>

## 🚀 **始め方**

### **Google Sheetsの場合:**
1. [こちら](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weOuttqDhiTCVcgA/edit?usp=sharing)をクリックしてチュートリアルにアクセス
2. シートをGoogle Driveにコピー
3. 「始め方」タブの指示に従ってください

### **Jupyter Notebooksの場合:**
1. このリポジトリをクローン
2. お好みのバージョンを選択（1P、Anthropic SDK、またはboto3）
3. `00_Tutorial_How-To.ipynb`ファイルのセットアップ指示に従ってください

<br>

## 📚 **チュートリアル章立て**

1. **基本的なプロンプト構造** - 構成要素を学ぶ
2. **明確で直接的であること** - 正確な指示を作る
3. **ロールプロンプティング** - 有用なペルソナを割り当てる
4. **データと指示の分離** - 入力を明確に構造化する
5. **出力のフォーマット** - Claudeの応答方法を制御する
6. **段階的思考** - 推論プロセスを導く
7. **例の使用** - Few-Shotプロンプティングを活用する
8. **幻覚の回避** - 応答を根拠に基づかせる
9. **複雑なプロンプト** - 洗練されたワークフローを構築する

**付録も含む:**
- プロンプトチェーン
- ツール使用と関数呼び出し
- 実証的パフォーマンス評価
- 検索と取得技術

<br>

## 🔧 **前提条件**

- **Google Sheetsバージョン:** Googleアカウントのみ
- **Jupyterノートブック:** PythonとJupyterの基本的な知識
- **APIアクセス:** AnthropicのAPIまたはAmazon Bedrock経由でClaudeへのアクセスが必要

<br>

## 💡 **成功のためのヒント**

- プロンプティングが初めての場合は**Google Sheetsバージョンから始める**
- **自由に実験する** - 例を修正してみる
- **説明を注意深く読む** - 技術が*なぜ*機能するかを理解することが重要
- チュートリアルを進めながら**自分の使用事例で練習する**

<br>

## 🤝 **貢献**

貢献を歓迎します！ガイドラインについては[CONTRIBUTING.md](./CONTRIBUTING.md)をご覧ください。

<br>

## 📄 **ライセンス**

このチュートリアルは[MITライセンス](./LICENSE)の下で公開されています。

---

**プロンプティングエキスパートになる準備はできましたか？** [Google Sheetsチュートリアル](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weOuttqDhiTCVcgA/edit?usp=sharing)から始めるか、Jupyterノートブックに飛び込んでください！

質問やフィードバックについては、このリポジトリにissueを開いてください。