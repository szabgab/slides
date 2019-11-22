import os
import shutil
import logging

def main():
    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s - %(levelname)-5s - %(funcName)s - %(name)s - %(message)s',
        datefmt = "%Y-%m-%d %H:%M:%S"
    )
    target = '.'
    source = '../slides/'
    target = os.path.abspath(target)
    target = os.path.join(target, 'manuscript')
    resources = os.path.join(target, 'resources')
    source = os.path.abspath(source)
    logging.info(f"target: {target}")
    logging.info(f"source: {source}")

    if os.path.exists(target):
        shutil.rmtree(target)
    os.mkdir(target)
    os.mkdir(resources)

    slides_file = os.path.join(source, 'slides.txt')
    with open(slides_file, 'r') as fh:
        for line in fh:
            line = line.rstrip("\n")
            #if line != "docker":
            #    continue
            logging.info(f"Processing slides of {line}")
            src_examples = os.path.join(source, line, 'examples')
            if os.path.exists(src_examples):
                for example in os.listdir(src_examples):
                    #print(example)
                    example_path = os.path.join(src_examples, example)
                    if os.path.isdir(example_path):
                        logging.debug(f"Copy dir {example_path}")
                        shutil.copytree(example_path, os.path.join(resources, 'examples', example))
                    else:
                        logging.error(f"{example_path}")
                        # TODO maybe I should not even handle this just let the code blow up so I will be forced to fix
                        # this

main()


