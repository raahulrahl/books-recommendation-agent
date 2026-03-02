# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""books_recommendation_agent - An Bindu Agent."""

from books_recommendation_agent.__version__ import __version__
from books_recommendation_agent.main import (
    handler,
    initialize_agent,
    initialize_all,
    initialize_mcp_tools,
    main,
)

__all__ = [
    "__version__",
    "handler",
    "initialize_agent",
    "initialize_all",
    "initialize_mcp_tools",
    "main",
]
