import sys


def get_config() -> dict:
    import yaml

    config = "config.yaml"
    with open(config, "r") as f:
        return yaml.safe_load(f)


def run_api():
    import uvicorn
    from api.main import API

    config = get_config()
    server = API(config.get("host"), config.get("token"), config.get("cookie"))
    host = "0.0.0.0"
    port = 8000

    uvicorn.run(server.app, host=host, port=port)


def run_downloader():
    import asyncio
    from downloader.main import Downloader
    from core.backend import Backend

    config = get_config()
    asyncio.run(
        Downloader(
            Backend(config.get("url"), config.get("token"), config.get("cookie")),
            int(config.get("concurrent_downloads", 1)),
            int(config.get("retry_delay_seconds", 5)),
        ).main()
    )


if _name_ == "_main_":
    if len(sys.argv) < 2:
        print("Usage: python run.py [api|download]")
        sys.exit(1)
    command = sys.argv[1].lower()
    if command == "api":
        run_api()
    elif command == "download":
        run_downloader()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)