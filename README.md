# chat

based on ollama-webui but reverting back to the most minimal chatbot possible

will be part of [mycelium](https://github.com/celiumai/mycelium)

completely private llm after setup.

use docker and or vm

have data export and imports

now for the rest of the people:

## Features ⭐

- 🖥️ **Intuitive Interface**: Our chat interface takes inspiration from ChatGPT, ensuring a user-friendly experience.

- 📱 **Responsive Design**: Enjoy a seamless experience on both desktop and mobile devices.

- ⚡ **Swift Responsiveness**: Enjoy fast and responsive performance.

- 🚀 **Effortless Setup**: Install seamlessly using Docker or Kubernetes (kubectl, kustomize or helm) for a hassle-free experience.

- 💻 **Code Syntax Highlighting**: Enjoy enhanced code readability with our syntax highlighting feature.

- ✒️🔢 **Full Markdown and LaTeX Support**: Elevate your LLM experience with comprehensive Markdown and LaTeX capabilities for enriched interaction.

- 🔒 **Backend Reverse Proxy Support**: Bolster security through direct communication between Ollama Web UI backend and Ollama. This key feature eliminates the need to expose Ollama over LAN. Requests made to the '/ollama/api' route from the web UI are seamlessly redirected to Ollama from the backend, enhancing overall system security.

- 📜 **Chat History**: Effortlessly access and manage your conversation history.

- 🤖 **Multiple Model Support**: Seamlessly switch between different chat models for diverse interactions.

- 📜 **Prompt Preset Support**: Instantly access preset prompts using the `/` command in the chat input. Load predefined conversation starters effortlessly and expedite your interactions. Effortlessly import prompts through [OllamaHub](https://ollamahub.com/) integration.


## coming soon (Plugin Store) and not true:

- 📚 **Local RAG Integration**: Dive into the future of chat interactions with the groundbreaking Retrieval Augmented Generation (RAG) support. This feature seamlessly integrates document interactions into your chat experience. You can load documents directly into the chat or add files to your document library, effortlessly accessing them using `#` command in the prompt. In its alpha phase, occasional issues may arise as we actively refine and enhance this feature to ensure optimal performance and reliability.
- 👍👎 **RLHF Annotation**: Empower your messages by rating them with thumbs up and thumbs down, facilitating the creation of datasets for Reinforcement Learning from Human Feedback (RLHF). Utilize your messages to train or fine-tune models, all while ensuring the confidentiality of locally saved data.
- 📥🗑️ **Download/Delete Models**: Easily download or remove models directly from the web UI.
- ⬆️ **GGUF File Model Creation**: Effortlessly create Ollama models by uploading GGUF files directly from the web UI. Streamlined process with options to upload from your machine or download GGUF files from Hugging Face.
- 🔄 **Multi-Modal Support**: Seamlessly engage with models that support multimodal interactions, including images (e.g., LLava).
- 🧩 **Modelfile Builder**: Easily create Ollama modelfiles via the web UI. Create and add characters/agents, customize chat elements, and import modelfiles effortlessly through [OllamaHub](https://ollamahub.com/) integration.
- ⚙️ **Many Models Conversations**: Effortlessly engage with various models simultaneously, harnessing their unique strengths for optimal responses. Enhance your experience by leveraging a diverse set of models in parallel.
- 💬 **Collaborative Chat**: Harness the collective intelligence of multiple models by seamlessly orchestrating group conversations. Use the `@` command to specify the model, enabling dynamic and diverse dialogues within your chat interface. Immerse yourself in the collective intelligence woven into your chat environment.
- 🔄 **Regeneration History Access**: Easily revisit and explore your entire regeneration history.
- 📤📥 **Import/Export Chat History**: Seamlessly move your chat data in and out of the platform.
- 🗣️ **Voice Input Support**: Engage with your model through voice interactions; enjoy the convenience of talking to your model directly. Additionally, explore the option for sending voice input automatically after 3 seconds of silence for a streamlined experience.
- ⚙️ **Fine-Tuned Control with Advanced Parameters**: Gain a deeper level of control by adjusting parameters such as temperature and defining your system prompts to tailor the conversation to your specific preferences and needs.
- 🔗 **External LLM Server Connection**: Seamlessly link to any hosted external llm server hosted on a different address.
- 🔐 **Role-Based Access Control (RBAC)**: Ensure secure access with restricted permissions; only authorized individuals can access your Ollama, and exclusive model creation/pulling rights are reserved for administrators.
- 🌟 **Continuous Updates**: We are committed to improving Ollama Web UI with regular updates and new features.
- 🌐 **Web Browsing Capability**: Experience the convenience of seamlessly integrating web content directly into your chat. Easily browse and share information without leaving the conversation.
- 🔄 **Function Calling**: Empower your interactions by running code directly within the chat. Execute functions and commands effortlessly, enhancing the functionality of your conversations.
- ⚙️ **Custom Python Backend Actions**: Empower your Ollama Web UI by creating or downloading custom Python backend actions. Unleash the full potential of your web interface with tailored actions that suit your specific needs, enhancing functionality and versatility.
- 🧠 **Long-Term Memory**: Witness the power of persistent memory in our agents. Enjoy conversations that feel continuous as agents remember and reference past interactions, creating a more cohesive and personalized user experience.
- 🧪 **Research-Centric Features**: Empower researchers in the fields of LLM and HCI with a comprehensive web UI for conducting user studies. Stay tuned for ongoing feature enhancements (e.g., surveys, analytics, and participant tracking) to facilitate their research.
- 📈 **User Study Tools**: Providing specialized tools, like heat maps and behavior tracking modules, to empower researchers in capturing and analyzing user behavior patterns with precision and accuracy.
- 📚 **Enhanced Documentation**: Elevate your setup and customization experience with improved, comprehensive documentation.

## setup

### dependency

install docker and make sure you have docker compose

### setup

run run.sh

### Acknowledgments

special thanks to ollama-webui

## License 📜

This project is licensed under the [MIT License](LICENSE)

