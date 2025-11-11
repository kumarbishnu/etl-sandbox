### ETL Sandbox

#### Requirements
- [uv](https://docs.astral.sh/uv/#installation)

### Instructions

- Install dependencies
```bash
uv sync
```

- Update `config/settings.toml`

- Check snowflake connection status
```bash
uv run check_connection
```