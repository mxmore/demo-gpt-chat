# Streamlit GPT-4.1 Chatbot 项目

本项目是一个基于Streamlit的Web聊天问答系统，后端集成GPT-4.1模型进行对话。

## 使用方法

1. 安装依赖：`pip install -r requirements.txt`

2. 运行项目：`streamlit run app.py`

## 主要依赖

- streamlit
- openai
- python-dotenv

## 功能简介

- 聊天问答界面
- GPT-4.1模型对话支持

## 注意事项

如需对接 Azure OpenAI，请在环境变量或`.env`文件中配置以下信息：

```env
AZURE_OPENAI_API_KEY=你的Azure OpenAI密钥
AZURE_OPENAI_ENDPOINT=https://你的资源名.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=你的部署名称
```
