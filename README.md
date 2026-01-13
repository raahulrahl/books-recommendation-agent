<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">books-recommender-agent</h1>

<p align="center">
  <strong>An intelligent AI agent that delivers personalized book suggestions based on reader preferences, favorite titles, genres, ratings, reviews, and upcoming releases. It analyzes input to curate tailored literary recommendations with detailed metadata like author, genre, plot summary, and ratings. Ideal for discovering new reads, genre-specific lists, or books similar to favorites, this agent helps users explore diverse fiction and non-fiction options with contextual, engaging suggestions</strong>
</p>

<p align="center">
  <a href="https://github.com/raahulrahl/books-recommender-agent/actions/workflows/main.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/raahulrahl/books-recommender-agent/main.yml?branch=main" alt="Build status">
  </a>
  <a href="https://img.shields.io/github/license/raahulrahl/books-recommender-agent">
    <img src="https://img.shields.io/github/license/raahulrahl/books-recommender-agent" alt="License">
  </a>
</p>

---

## 📖 Overview

An intelligent AI agent that delivers personalized book suggestions based on reader preferences, favorite titles, genres, ratings, reviews, and upcoming releases. It analyzes input to curate tailored literary recommendations with detailed metadata like author, genre, plot summary, and ratings. Ideal for discovering new reads, genre-specific lists, or books similar to favorites, this agent helps users explore diverse fiction and non-fiction options with contextual, engaging suggestions. Built on the [Bindu Agent Framework](https://github.com/getbindu/bindu) for the Internet of Agents.

**Key Capabilities:**
- � Personalized book recommendations using Exa search
- 🎯 Analysis of reader preferences and reading history
- ⭐ Integration of ratings and reviews from Goodreads/StoryGraph
- � Detailed book metadata including genres, awards, and content warnings
- 🔮 Support for diverse genres and author perspectives

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) package manager
- API keys for OpenRouter and Mem0 (both have free tiers)

### Installation

```bash
# Clone the repository
git clone https://github.com/raahulrahl/books-recommender-agent.git
cd books-recommender-agent

# Create virtual environment
uv venv --python 3.12.9
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync

# Configure environment
cp .env.example .env
```

### Configuration

Edit `.env` and add your API keys:

| Key | Get It From | Required |
|-----|-------------|----------|
| `OPENROUTER_API_KEY` | [OpenRouter](https://openrouter.ai/keys) | ✅ Yes |
| `MEM0_API_KEY` | [Mem0 Dashboard](https://app.mem0.ai/dashboard/api-keys) | If you want to use Mem0 tools |

### Run the Agent

```bash
# Start the agent
uv run python -m books_recommender_agent

# Agent will be available at http://localhost:3773
```

### Github Setup

```bash
# Initialize git repository and commit your code
git init -b main
git add .
git commit -m "Initial commit"

# Create repository on GitHub and push (replace with your GitHub username)
gh repo create raahulrahl/books-recommender-agent --public --source=. --remote=origin --push
```

---

## 💡 Usage

### Example Queries

```bash
# Get personalized recommendations
"I loved The Night Circus and The Invisible Life of Addie LaRue. Can you recommend similar books?"

# Genre-specific search
"Recommend 5 fantasy books with strong female protagonists published in the last 2 years"

# Based on preferences
"I enjoy literary fiction with magical realism elements, around 300-400 pages"
```

### Input Formats

**Plain Text:**
```
I'm looking for mystery novels similar to Agatha Christie with modern settings
```

**JSON:**
```json
{
  "role": "user",
  "content": "Recommend science fiction books with themes of AI and consciousness"
}
```

### Output Structure

The agent returns structured output with:
- **Book Recommendations**: Title, author, publication year
- **Detailed Metadata**: Genre, ratings, page count, awards
- **Summaries**: Engaging plot descriptions and content advisories
- **Additional Info**: Series information, similar authors, audiobook availability

---

## 🔌 API Usage

The agent exposes a RESTful API when running. Default endpoint: `http://localhost:3773`

### Quick Start

For complete API documentation, request/response formats, and examples, visit:

📚 **[Bindu API Reference - Send Message to Agent](https://docs.getbindu.com/api-reference/all-the-tasks/send-message-to-agent)**


### Additional Resources

- 📖 [Full API Documentation](https://docs.getbindu.com/api-reference/all-the-tasks/send-message-to-agent)
- 📦 [Postman Collections](https://github.com/GetBindu/Bindu/tree/main/postman/collections)
- 🔧 [API Reference](https://docs.getbindu.com)

---

## 🎯 Skills

### personalized-book-recommendation (v1.0.0)

**Primary Capability:**
- Curates personalized book recommendations using Exa search
- Analyzes reader preferences and reading patterns
- Provides comprehensive book metadata and ratings

**Features:**
- Exa-powered book discovery and search
- Goodreads/StoryGraph rating integration
- Content warnings and trigger advisories
- Series information and author suggestions
- Markdown-formatted recommendations with emoji indicators

**Best Used For:**
- Finding books similar to favorites
- Genre-specific recommendations
- Discovering new authors and diverse perspectives
- Getting detailed book information with ratings

**Not Suitable For:**
- Academic paper recommendations
- Technical documentation searches
- Non-book media recommendations

**Performance:**
- Average processing time: ~1-2 seconds
- Max concurrent requests: 10
- Memory per request: 256MB

---

## 🐳 Docker Deployment

### Local Docker Setup

```bash
# Build and run with Docker Compose
docker-compose up --build

# Agent will be available at http://localhost:3773
```

### Docker Configuration

The agent runs on port `3773` and requires:
- `OPENROUTER_API_KEY` environment variable
- `MEM0_API_KEY` environment variable

Configure these in your `.env` file before running.

### Production Deployment

```bash
# Use production compose file
docker-compose -f docker-compose.prod.yml up -d
```

---

## 🌐 Deploy to bindus.directory

Make your agent discoverable worldwide and enable agent-to-agent collaboration.

### Setup GitHub Secrets

```bash
# Authenticate with GitHub
gh auth login

# Set deployment secrets
gh secret set BINDU_API_TOKEN --body "<your-bindu-api-key>"
gh secret set DOCKERHUB_TOKEN --body "<your-dockerhub-token>"
```

Get your keys:
- **Bindu API Key**: [bindus.directory](https://bindus.directory) dashboard
- **Docker Hub Token**: [Docker Hub Security Settings](https://hub.docker.com/settings/security)

### Deploy

```bash
# Push to trigger automatic deployment
git push origin main
```

GitHub Actions will automatically:
1. Build your agent
2. Create Docker container
3. Push to Docker Hub
4. Register on bindus.directory

---

## 🛠️ Development

### Project Structure

```
books-recommender-agent/
├── books_recommender_agent/
│   ├── skills/
│   │   └── books_recommender_agent/
│   │       ├── skill.yaml          # Skill configuration
│   │       └── __init__.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── main.py                     # Agent entry point
│   └── agent_config.json           # Agent configuration
├── tests/
│   └── test_main.py
├── .env.example
├── docker-compose.yml
├── Dockerfile.agent
└── pyproject.toml
```

### Running Tests

```bash
make test              # Run all tests
make test-cov          # With coverage report
```

### Code Quality

```bash
make format            # Format code with ruff
make lint              # Run linters
make check             # Format + lint + test
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
uv run pre-commit install

# Run manually
uv run pre-commit run -a
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Powered by Bindu

Built with the [Bindu Agent Framework](https://github.com/getbindu/bindu)

**Why Bindu?**
- 🌐 **Internet of Agents**: A2A, AP2, X402 protocols for agent collaboration
- ⚡ **Zero-config setup**: From idea to production in minutes
- 🛠️ **Production-ready**: Built-in deployment, monitoring, and scaling

**Build Your Own Agent:**
```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

---

## 📚 Resources

- 📖 [Full Documentation](https://raahulrahl.github.io/books-recommender-agent/)
- 💻 [GitHub Repository](https://github.com/raahulrahl/books-recommender-agent/)
- 🐛 [Report Issues](https://github.com/raahulrahl/books-recommender-agent/issues)
- 💬 [Join Discord](https://discord.gg/3w5zuYUuwt)
- 🌐 [Agent Directory](https://bindus.directory)
- 📚 [Bindu Documentation](https://docs.getbindu.com)

---

<p align="center">
  <strong>Built with 💛 by the team from Amsterdam 🌷</strong>
</p>

<p align="center">
  <a href="https://github.com/raahulrahl/books-recommender-agent">⭐ Star this repo</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Join Discord</a> •
  <a href="https://bindus.directory">🌐 Agent Directory</a>
</p>
