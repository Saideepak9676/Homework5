class App:
    @staticmethod
    def start() -> None:
        print("Hello World. Type 'exit' to exit.")

        keep_running = True
        while keep_running:
            user_input = input(">>> ").strip().lower()
            if user_input == "exit":
                print("Exiting...")
                keep_running = False
            else:
                print("Unknown command. Type 'exit' to exit.")
