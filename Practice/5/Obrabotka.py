def open_file(filename: str):
    try:
        file = open(filename, "r",encoding="utf-8")
        count = int(file.readline())
        numbers_list: list = file.read().splitlines()
        if len(numbers_list) != count:
            raise Exception
        numbers_list = [int(numbers_list[i]) for i in range(0, count)]
        return numbers_list
    except FileNotFoundError:
        return("Такого файла нет")
    except ValueError:
        return(f"В файле обнаружены посторонние символы")
    except Exception:
        return(f"Количество не совпадает")
    finally:
        file.close()
