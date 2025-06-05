# プロンプトエンジニアリングチュートリアル セットアップガイド

## 環境構築手順

### 1. 仮想環境の作成と有効化

```bash
# 仮想環境を作成
python -m venv prompt_env

# 仮想環境を有効化
# macOS/Linux:
source prompt_env/bin/activate

# Windows:
prompt_env\Scripts\activate
```

### 2. パッケージのインストール

```bash
# 必要なパッケージをインストール
pip install -r requirements.txt
```

### 3. API キーの設定

1. `.env`ファイルを作成：
```
ANTHROPIC_API_KEY=your_actual_api_key_here
MODEL_NAME=claude-3-sonnet-20240229
```

2. または環境変数として設定：
```bash
export ANTHROPIC_API_KEY="your_actual_api_key_here"
```

### 4. Jupyter Notebookの起動

```bash
jupyter notebook
```

## トラブルシューティング

### `externally-managed-environment`エラーが発生した場合

このエラーはPEP 668により、システムのPython環境でのパッケージインストールが制限されているために発生します。

**解決方法：**
1. 上記の仮想環境を使用する方法
2. `--user`フラグを使用してユーザー領域にインストール：
   ```bash
   pip install --user anthropic
   ```
3. `--break-system-packages`フラグを使用（非推奨）：
   ```bash
   pip install --break-system-packages anthropic
   ```

### その他の問題

- **API キーエラー**: 正しいAPI キーが設定されているかを確認
- **モデル名エラー**: 最新のモデル名を使用しているかを確認
- **IPython storeエラー**: 環境変数の使用に切り替える 