def open_file(filename: str):
    opened = False
    try:
        file = open(filename, "r")
        opened = True
        count = int(file.readline())
        return [int(x) for x in [file.readline() for _ in range(count)]]
    except FileNotFoundError:
        print("Такого файла нет")
    except ValueError:
        print(f"В файле обнаружены посторонние символы")
    except Exception as e:
        print(f"Кхм... Ошибка не опознана {type(e)}, {e=}")
    finally:
        if opened:
            file.close()