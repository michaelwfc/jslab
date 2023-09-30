"""main.py"""


def main():
    from enviroments import set_gpt_env
    from server import run_server
    set_gpt_env()
    run_server()


if __name__ == "__main__":
    main()
