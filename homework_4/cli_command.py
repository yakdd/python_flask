import argparse
import task_9_threads
import task_9_multiprocessing
import task_9_async

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image loader')
    parser.add_argument('links', type=str, nargs='+', help='Input link to the image')
    args = parser.parse_args()
    task_9_threads.main(args.links)
    task_9_multiprocessing.main(args.links)
    task_9_async.main(args.links)
