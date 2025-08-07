# VOICEROID Conversation System

This repository contains a simple conversation system for interacting with
[VOICEROID2](https://www.ah-soft.com/product/voiceroid2/) using the
voice of **Akari Kizuna (\u7d32\u661f\u3042\u304b\u308a)**. It is based on the article
\u300e\u3010\u65b0\u6642\u9593\u3067\u4f5c\u308b!!\u3011VOICEROID\u3068\u4f1a\u8a71\u3057\u305f\u304b\u3063\u305f\u306e\u3067Python\u4f1a\u8a71\u30b7\u30b9\u30c6\u30e0\u3092\u4f5c\u308bv1\u3011\u7d32\u661f\u3042\u304b\u308a\u3068\u304a\u558b\u308a\u3057\u305f\u3044!!\u3011\u300f
(https://qiita.com/hidepy/items/bcd31e6b4b75415495ac) and wraps up the
code into a ready\u2011to\u2011use repository. After cloning this repository and
providing your own MEBO API credentials, you can chat with Akari by
saying something into your microphone and hearing a spoken reply.

## Features

* Record Japanese speech via your microphone and transcribe it using the
  Google Speech Recognition service.
* Send the transcribed text to the [MEBO API](https://api-mebo.dev/)
  to generate a conversational response.
* Use **SeikaSay2.exe** (part of the [AssistantSeika](https://voicepeak.jp/assistantseika/)
  suite) to synthesize the response with Akari’s voice.
* Modular design with separate scripts for capturing audio (`main.py`) and
  generating/speaking the reply (`voiceroid_speaks.py`).

## Prerequisites

Before you can run this project, you will need:

1. **Python 3.8+** installed on your system.
2. A working **microphone** connected to your computer.
3. The **AssistantSeika** software installed and activated.
   * Copy or note the full path to `SeikaSay2.exe` (e.g.,
     `C:\\Program Files\\AssistantSeika\\SeikaSay2\\SeikaSay2.exe`).
4. A valid **MEBO API key, agent ID and UID**. You can obtain these by
   creating a bot at <https://api-mebo.dev/>.

## Installation

1. **Clone this repository**:

   ```bash
   git clone https://github.com/YOUR_USERNAME/voiceroid_conversation_system.git
   cd voiceroid_conversation_system
   ```

2. **Create and activate a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Edit `voiceroid_speaks.py`**:

   Open `voiceroid_speaks.py` in your text editor and replace the
   placeholder strings `<YOUR-APIKEY-HERE>`, `<YOUR-AGENTID-HERE>` and
   `<YOUR-UID-HERE>` with the credentials you obtained from MEBO. Also
   update the `SEIKASAY_EXE` constant to point to your `SeikaSay2.exe`.

   ```python
   API_KEY = "your-api-key"
   AGENT_ID = "your-agent-id"
   UID = "your-user-id"
   SEIKASAY_EXE = r"C:\\Path\\To\\SeikaSay2.exe"
   ```

## Usage

Once everything is configured, you can start a conversation with Akari by
running `main.py`. The script will listen for your speech, transcribe
it to Japanese text and then hand it off to `voiceroid_speaks.py` to
generate and speak a response.

```bash
python main.py
```

You should see a prompt saying “あかりちゃんへの質問を喹ってね:”. Speak your
question into the microphone. If the speech is recognized, Akari will
reply via VOICEROID. If the speech cannot be recognized, a fallback
message will be printed.

### Example session

```
あかりちゃんへの質問を喹ってね:
-----------detect!----------
 今日は天気がいいね
request_msg: 今日は天気がいいね
response_msg: そうですね。お散歩に出かけてみましょうか。
```

You will hear Akari say: “回答は、そうですね。お散歩に出かけてみましょうか。”

## Notes

* **Speech Recognition API** – This project uses the default Google
  Speech Recognition API provided by the `speech_recognition` library. If
  you hit usage limits or prefer an offline recognizer, consider
  configuring a different recognizer as documented in the
  `speech_recognition` package.
* **VOICEROID voice selection** – The `-cid 2004` flag passed to
  `SeikaSay2.exe` selects the Akari voice. If you wish to use a
  different voice, consult the AssistantSeika documentation for the
  appropriate character ID.

## License

This project reimplements code published on Qiita by @hidepy for
educational purposes. See the original article for more context. You are
free to use and modify this code under the terms of the MIT license.
