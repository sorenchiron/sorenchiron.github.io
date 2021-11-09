import imageio
import argparse
import cv2
import os

parser = argparse.ArgumentParser('GIF image size adjust program')
parser.add_argument('input',type=str,default=None,help='input gif image path')
parser.add_argument('scale',type=float,default=1,help='scale ratio to be applied to the input gif image, float number.')
parser.add_argument('-d','--duration',dest='duration',default=0.1,help='frame duration')
parser.add_argument('--dry',action='store_true',default=False,help='do everthing except actuall system calls')
parser.add_argument('--open',action='store_true',default=False,help='open the file after creation')
args = parser.parse_args()

def log(*argv):
    print('--Log:',*argv)

def get_dir_fname_suffix(path):
    ''''''
    dirname = os.path.dirname(path)
    basename = os.path.basename(path)
    if not '.' in basename:
        fname = basename
        suffix = None
    else:
        suffix = basename.split('.')[-1]
        fname = basename[:-len(suffix)-1]
    return dirname,fname,suffix

def fname_add_tag(path,tag):
    d,f,s = get_dir_fname_suffix(path)
    return os.path.join(d,f'{f}_{tag}.{s}')

def main():
    series = imageio.mimread(args.input)
    series_len = len(series)
    shape = series[0].shape
    h,w,*c = shape
    nh,nw = int(h*args.scale),int(w*args.scale)
    new_series = [cv2.resize(i,(nw,nh),cv2.INTER_CUBIC) for i in series]
    new_shape = new_series[0].shape
    new_path = fname_add_tag(args.input,'LD')
    if args.dry:
        log('original frames',series_len)
        log('original frame size',shape)
        log('new size',new_shape)
        log('out path',new_path)
        log('nothing is done.')
    else:
        imageio.mimsave(new_path,new_series,duration=args.duration)
        log('finished')
    return 0

if __name__ == '__main__':
    main()