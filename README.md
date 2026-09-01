# AI Voice Assistant V3

> Version 3 of an AI-powered Voice Assistant with advanced audio processing, natural language understanding, and conversation capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Module Documentation](#module-documentation)

## 🎯 Overview

The AI Voice Assistant V3 is a sophisticated voice interaction system that combines multiple AI technologies to create a natural conversational experience. It processes audio input, detects voice activity, recognizes wake words, classifies user intent, and generates intelligent responses.

### Key Features

- **Real-time Audio Processing**: Capture and process audio streams with support for various sample rates and channels
- **Voice Activity Detection (VAD)**: Detect speech in audio input efficiently
- **Wake Word Detection**: Listen for specific wake words before processing commands
- **Intent Classification**: Understand user intent (conversation vs. commands)
- **Multi-Backend LLM Support**: Flexible language model integration via Ollama
- **Memory Management**: Context-aware conversation memory with semantic search
- **Text-to-Speech**: Convert responses back to natural audio
- **RESTful API**: FastAPI-based HTTP endpoints for integration
- **WebSocket Support**: Real-time bidirectional communication
- **Comprehensive Logging**: Detailed application and error logging

## 🏗️ Architecture

The application follows a layered, modular architecture with clear separation of concerns:

```
┌─────────────────────────────────────────┐
│         API Layer (FastAPI)              │
│  ├─ HTTP Routes & WebSocket Manager     │
│  └─ Request/Response Handling            │
├─────────────────────────────────────────┤
│       Assistant Layer (Orchestration)    │
│  ���─ Voice Activity Detection             │
│  ├─ Wake Word Detection                  │
│  ├─ Intent Classification                │
│  └─ Conversation Routing                 │
├─────────────────────────────────────────┤
│         Core Modules (Features)          │
│  ├─ Audio Processing                     │
│  ├─ LLM Integration                      │
│  ├─ Memory/Context Management            │
│  ├─ Conversation Management              │
│  └─ Configuration & Logging              │
├─────────────────────────────────────────┤
│         Data Layer (Persistence)         │
│  ├─ SQLite Database (ORM)                │
│  └─ Vector Database (Chroma)             │
└─────────────────────────────────────────┘
```

## 📁 Project Structure

```
AI-Voice-Assistant-V3/
├── app/                          # Main application package
│   ├── api/                      # REST API & WebSocket layer
│   ├── assistant/                # Core orchestration logic
│   ├── audio/                    # Audio input/output processing
│   ├── config/                   # Configuration management
│   ├── conversation/             # Conversation management
│   ├── core/                     # Core utilities and DI container
│   ├── database/                 # Database models & sessions
│   ├── llm/                      # Language model integration
│   ├── logger/                   # Logging configuration
│   ├── memory/                   # Memory & context management
│   ├── models/                   # Pydantic data models
│   ├── pipeline/                 # Data processing pipelines
│   ├── prompts/                  # LLM prompt templates
│   ├── runtime/                  # Runtime environment setup
│   ├── scripts/                  # Utility scripts
│   └── ui/                       # User interface components
├── schemas/                      # Request/response schemas
├── tests/                        # Test suite
├── main.py                       # Application entry point
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment configuration template
└── pytest.ini                    # Pytest configuration
```

---

## 🗂️ Module Documentation

### **app/api/** - REST API & WebSocket Layer

Handles all HTTP and WebSocket communication with the client.

**Files:**
- `app.py` - FastAPI application initialization and setup
- `dependencies.py` - Dependency injection for API endpoints
- `schemas.py` - Request/response Pydantic schemas
- `websocket_manager.py` - WebSocket connection management
- `routers/` - Organized API endpoint definitions

**Purpose:** Provides HTTP/WebSocket interfaces for the AI assistant, enabling clients to send audio and receive responses in real-time.

**Key Responsibilities:**
- Route incoming API requests
- Manage WebSocket connections
- Validate request/response payloads
- Handle connection lifecycle events

---

### **app/assistant/** - Core Orchestration

Main orchestrator that coordinates all components of the assistant pipeline.

**Files:**
- `manager.py` - AssistantManager class (main orchestrator)
- `models.py` - AssistantResponse data models
- `pipeline.py` - Assistant processing pipeline definition
- `intents/` - Intent classification system
  - `classifier.py` - Intent classification logic
  - `models.py` - Intent types and classifications
- `skills/` - Extensible skill system for commands

**Purpose:** Orchestrates the entire conversation flow from audio input to text response.

**Key Responsibilities:**
- Coordinate voice activity detection
- Manage wake word detection
- Route to appropriate handlers (conversation vs. commands)
- Return structured responses

**Processing Flow:**
```
Audio Input
    ↓
Voice Activity Detection
    ↓ (if speech detected)
Wake Word Detection
    ↓ (if wake word found)
Intent Classification
    ↓
Route Handler
├─ CONVERSATION → ConversationManager
└─ COMMAND → Skill Router
    ↓
Response Generation
```

---

### **app/audio/** - Audio I/O & Processing

Comprehensive audio handling including recording, playback, and AI-powered processing.

**Files:**
- `models.py` - Audio data structures
  - `AudioChunk` - Represents a piece of audio
  - `TranscriptionResult` - Speech-to-text results
- `interfaces.py` - Abstract interfaces for audio components
- `manager.py` - Audio management (currently empty, awaiting implementation)

**Subdirectories:**
- `recorder/` - Audio input capture from microphone/files
- `player/` - Audio output playback system
- `stt/` - Speech-to-Text (transcription) engines
  - Uses Faster-Whisper for efficient transcription
- `tts/` - Text-to-Speech (voice synthesis)
  - Uses Kokoro for natural voice generation
- `vad/` - Voice Activity Detection
  - Detects presence of human speech
- `wakeword/` - Wake word detection
  - Listens for specific activation phrases

**Purpose:** Handles all audio I/O operations and preprocessing.

**Key Responsibilities:**
- Capture audio from input devices
- Convert audio formats and sample rates
- Transcribe speech to text
- Synthesize text to speech
- Detect voice presence and wake words

---

### **app/config/** - Configuration Management

Centralizes all application configuration from environment variables.

**Purpose:** Manages environment-based configuration using Pydantic settings.

**Key Responsibilities:**
- Load configuration from `.env` files
- Validate configuration values
- Provide typed access to settings throughout the app

**Configuration Options:**
- `APP_NAME` - Application display name
- `APP_ENV` - Environment (development/production)
- `DEBUG` - Debug mode flag
- `HOST` / `PORT` - API server settings
- `OLLAMA_HOST` - LLM service endpoint
- `OLLAMA_MODEL` - Model name for inference
- `EMBEDDING_MODEL` - Model for semantic embeddings
- `SQLITE_DB` - Database file path
- `CHROMA_DB` - Vector database path
- `LOG_LEVEL` - Logging verbosity
- `STT_MODEL` - Speech recognition model
- `TTS_VOICE` - Text-to-speech voice selection

---

### **app/conversation/** - Conversation Management

Manages the conversational flow and context between user and assistant.

**Files:**
- `manager.py` - ConversationManager for handling chats
- `models.py` - Conversation data structures

**Purpose:** Handles multi-turn conversations with context awareness.

**Key Responsibilities:**
- Maintain conversation history
- Retrieve relevant memory/context
- Call LLM for response generation
- Format and return responses

---

### **app/core/** - Core Utilities & DI Container

Provides foundational utilities and dependency injection configuration.

**Files:**
- `container.py` - Dependency Injection container (IoC pattern)
- `lifecycle.py` - Application startup/shutdown events
- `exceptions.py` - Custom exception definitions

**Purpose:** Centralizes component initialization and wiring.

**Key Responsibilities:**
- Initialize all major components
- Wire dependencies between modules
- Manage component lifecycle
- Provide factory methods for creating instances

**Components Initialized:**
- Configuration manager
- Database connections
- Audio processors (STT, TTS, VAD, etc.)
- LLM manager
- Memory manager
- Logger
- Assistant manager

---

### **app/database/** - Data Persistence Layer

Manages database operations for storing conversation history and metadata.

**Files:**
- `base.py` - SQLAlchemy declarative base
- `database.py` - Database connection and session management
- `models.py` - SQLAlchemy ORM models
- `session.py` - Database session factory

**Technology Stack:**
- **ORM**: SQLAlchemy
- **Database**: SQLite (async via aiosqlite)
- **Pattern**: Session-based transaction management

**Purpose:** Provides persistent storage for:
- Conversation history
- User metadata
- System logs
- Session information

---

### **app/llm/** - Language Model Integration

Abstracts LLM interactions with pluggable provider support.

**Files:**
- `interfaces.py` - Abstract LLM interfaces
  - `LLMInterface` - Core LLM contract
  - `EmbeddingInterface` - Embedding generation
- `factory.py` - Factory for creating LLM instances
- `manager.py` - LLMManager for coordinating requests
- `models.py` - LLM response structures

**Subdirectories:**
- `providers/` - Specific LLM implementations
  - Ollama integration (primary provider)
  - Extensible for other providers
- `prompts/` - Prompt templates and engineering

**Purpose:** Provides unified interface to language models.

**Key Responsibilities:**
- Abstract LLM provider differences
- Handle inference requests
- Generate embeddings for semantic search
- Manage model lifecycle
- Cache responses when appropriate

**Supported Backends:**
- **Ollama** (primary): Local or remote inference
- Extensible architecture for: OpenAI, Anthropic, etc.

---

### **app/logger/** - Logging Configuration

Centralized logging setup using loguru.

**Files:**
- `logger.py` - Logger configuration and setup

**Purpose:** Provides structured, consistent logging throughout the application.

**Features:**
- Configurable log levels
- Structured logging format
- File rotation support
- Performance logging

---

### **app/memory/** - Context & Memory Management

Sophisticated memory system supporting multiple types of memories with semantic search.

**Files:**
- `interfaces.py` - Abstract memory interfaces
  - `Memory` - Core memory interface
  - `MemoryProvider` - Storage backend interface
- `manager.py` - MemoryManager for coordinating memory operations
- `models.py` - Memory data structures
- `mappers.py` - Memory object mapping utilities
- `exceptions.py` - Memory-specific exceptions

**Subdirectories:**
- `providers/` - Memory storage backends
  - Chroma (vector database)
  - SQLite (relational storage)
- `services/` - Memory query and retrieval services
- `working/` - Working/short-term memory

**Purpose:** Maintains context for multi-turn conversations.

**Memory Types:**
- **Short-term (Working)**: Current conversation context
- **Long-term (Semantic)**: Conversation history with embeddings
- **Facts**: Persistent knowledge about user preferences
- **Sessions**: Conversation session metadata

**Key Responsibilities:**
- Store conversation exchanges
- Retrieve relevant context
- Semantic search over memories
- Clean up old memories
- Summarize long conversations

---

### **app/models/** - Pydantic Data Models

Shared data models for type safety and validation.

**Purpose:** Defines all request/response and internal data structures.

**Contains:**
- Audio models
- Assistant request/response models
- Memory models
- API schema definitions

---

### **app/pipeline/** - Data Processing Pipelines

Orchestrates multi-step data processing workflows.

**Purpose:** Chains together audio processing, inference, and response generation steps.

---

### **app/prompts/** - LLM Prompt Templates

Stores prompt engineering templates for various use cases.

**Purpose:** Centralizes prompt templates for:
- System prompts
- Few-shot examples
- Instruction templates
- Memory summarization

---

### **app/runtime/** - Runtime Environment Setup

Configures the runtime environment on application startup.

**Purpose:** Handles:
- Environment validation
- Path creation (data directories, logs)
- Dependency pre-loading

---

### **app/scripts/** - Utility Scripts

Standalone scripts for maintenance and development.

**Purpose:** May contain:
- Database initialization
- Model downloading
- Data migration
- Debugging utilities

---

### **app/ui/** - User Interface Components

Frontend or UI-related code for client interfaces.

**Purpose:** May contain:
- Web UI components (if using web frontend)
- Terminal UI helpers
- Visualization utilities

---

### **schemas/** - Data Schemas

Request/response schemas (alternative location from api/).

**Files:**
- `chat.py` - Chat request/response schemas
- `speech.py` - Speech/audio schemas
- `memory.py` - Memory query/response schemas
- `health.py` - Health check schemas
- `tool.py` - Tool use schemas

**Purpose:** Pydantic models for API contract validation.

---

### **tests/** - Test Suite

Comprehensive test coverage using pytest.

**Subdirectories:**
- `assistant/` - Assistant manager tests
- `audio/` - Audio processing tests
- `conversation/` - Conversation flow tests
- `memory/` - Memory system tests

**Files:**
- `conftest.py` - Pytest fixtures and configuration

**Purpose:** Ensures code quality and correctness.

**Testing Tools:**
- `pytest` - Test framework
- `pytest-asyncio` - Async test support
- `httpx` - HTTP client for API testing

---

## 📦 Installation

### Prerequisites

- Python 3.11+
- Ollama (for LLM inference) - https://ollama.ai
- Audio device (microphone/speakers)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MeerBaloch7/AI-Voice-Assistant-V3.git
   cd AI-Voice-Assistant-V3
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Ollama:**
   ```bash
   # Download and install from https://ollama.ai
   # Start Ollama service
   ollama serve
   
   # In another terminal, pull the required model
   ollama pull qwen2  # or your preferred model
   ```

---

## ⚙️ Configuration

1. **Copy the example environment file:**
   ```bash
   cp .env.example .env
   ```

2. **Configure the `.env` file:**

   ```env
   # Application Settings
   APP_NAME=AI Assistant V3
   APP_ENV=development
   DEBUG=true
   
   # API Settings
   HOST=127.0.0.1
   PORT=8000
   
   # LLM Configuration
   OLLAMA_HOST=http://localhost:11434
   OLLAMA_MODEL=qwen2           # Change to your preferred model
   
   # Embedding Model (for semantic search)
   EMBEDDING_MODEL=nomic-embed-text
   
   # Database Paths
   SQLITE_DB=data/sqlite/assistant.db
   CHROMA_DB=data/chroma
   
   # Audio Settings
   STT_MODEL=base                # Whisper model size (tiny/base/small/medium)
   TTS_VOICE=af_bella            # Voice name for text-to-speech
   
   # Logging
   LOG_LEVEL=INFO
   ```

3. **Create data directories:**
   ```bash
   mkdir -p data/sqlite data/chroma logs
   ```

---

## 🚀 Running the Application

### Start the API Server

```bash
python main.py
```

The API will be available at: `http://localhost:8000`

### Interactive Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### API Endpoints

The exact endpoints depend on the router configuration, but typically include:

- `POST /api/chat` - Send a text message
- `POST /api/speech` - Process speech/audio
- `GET /api/health` - Health check
- `WebSocket /ws` - Real-time communication

---

## 🧪 Testing

### Run All Tests

```bash
pytest
```

### Run Specific Test Module

```bash
pytest tests/assistant/
pytest tests/audio/
pytest tests/memory/
```

### Run with Coverage

```bash
pytest --cov=app tests/
```

### Run a Single Test

```bash
pytest tests/audio/test_transcription.py::test_transcribe_audio
```

### Pytest Configuration

The `pytest.ini` file contains test settings including:
- Test discovery patterns
- Async test markers
- Output formats
- Coverage settings

---

## 🔄 Data Flow Example

### Speech to Response Flow

```
1. Audio Input (user speaks)
   └─> AudioChunk { path, sample_rate, channels }

2. Voice Activity Detection (VAD)
   └─> VoiceActivityManager.detect()
   └─> "Is speech present?"

3. Wake Word Detection & Transcription
   └─> WakeWordManager.detect()
   └─> "Did you say the wake word?"
   └─> TranscriptionResult { text: "user input" }

4. Intent Classification
   └─> IntentClassifier.classify("user input")
   └─> IntentType.CONVERSATION | COMMAND

5. Route to Handler
   ├─ CONVERSATION
   │  └─> ConversationManager.chat(text)
   │     └─> MemoryManager.retrieve_context()
   │     └─> LLMManager.generate_response()
   └─ COMMAND
      └─> SkillRouter.execute_command()

6. Text-to-Speech
   └─> TTSManager.synthesize(response_text)
   └─> Audio Output

7. Response
   └─> AssistantResponse { user_text, assistant_text }
```

---

## 📊 Key Dependencies

| Package | Purpose |
|---------|---------|
| `fastapi` | Web framework |
| `uvicorn` | ASGI server |
| `pydantic` | Data validation |
| `faster-whisper` | Speech recognition |
| `ollama` | LLM inference client |
| `chromadb` | Vector database |
| `sqlalchemy` | ORM |
| `sentence-transformers` | Text embeddings |
| `kokoro` | Text-to-speech |
| `loguru` | Structured logging |
| `sounddevice` | Audio I/O |
| `pyautogui` / `mss` / `easyocr` | Computer vision (for screen-reading commands) |

---

## 🛠️ Development Tips

### Adding a New Skill

1. Create a new file in `app/assistant/skills/`
2. Implement the `BaseSkill` interface
3. Register in the SkillRouter
4. Add tests in `tests/assistant/`

### Adding a New Memory Provider

1. Implement `MemoryProvider` interface in `app/memory/providers/`
2. Register in the MemoryManager
3. Add migration if using database

### Adding a New LLM Provider

1. Implement `LLMInterface` in `app/llm/providers/`
2. Update factory to recognize new provider
3. Add configuration in `.env`

---

## 📝 License

This project is part of the AI-Voice-Assistant series.

---

## 👤 Author

Created by **MeerBaloch7**

GitHub: https://github.com/MeerBaloch7

---

## 🐛 Troubleshooting

### Common Issues

**Ollama Connection Error**
```
Error: Cannot connect to Ollama at http://localhost:11434
Solution: Ensure Ollama is running (ollama serve) and accessible
```

**Audio Device Not Found**
```
Error: No audio input device available
Solution: Check audio device settings, install sounddevice drivers
```

**Database Lock**
```
Error: Database is locked
Solution: Ensure only one instance is running, check for zombie processes
```

**Model Download Issues**
```
Solution: Manually run: ollama pull [model-name]
```

---

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [Chroma Documentation](https://docs.trychroma.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---

## 🤝 Contributing

Contributions welcome! Please:

1. Create a feature branch
2. Add tests for new functionality
3. Update documentation
4. Submit a pull request

---

**Last Updated:** September 1, 2026
