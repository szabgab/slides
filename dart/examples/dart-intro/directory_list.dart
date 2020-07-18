import 'dart:io';
void main() {
    var myDir = Directory.current;
    print(myDir);

    myDir.list()
        .listen((FileSystemEntity entity) {
            print(entity.path);
    });
}

