def mock_searxng_search(query: str):
    q = query.lower()

    if "crypto" in q:
        return "Bitcoin hits new all-time high amid ETF approvals."
    if "ai" in q:
        return "Open-source AI models challenge proprietary leaders."
    if "market" in q or "rates" in q:
        return "Fed signals rate pause as equities rally."

    return "Global tech and policy debates dominate headlines."