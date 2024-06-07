def humanize_size(file_size):
        unit_type_map = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        ctr = 0

        while file_size > 1024:
            if ctr <= len(unit_type_map):
                file_size = file_size / 1024
                ctr += 1
            else:
                break
            
        return str(round(file_size)) + " " + unit_type_map[ctr]