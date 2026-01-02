import { useRef, useState } from 'react';
import { Upload, Loader2 } from 'lucide-react';
import { extractPhotoData } from '../utils/exifExtractor';
import type { Photo } from '../types';

interface PhotoUploaderProps {
  onPhotosUploaded: (photos: Photo[]) => void;
}

export default function PhotoUploader({ onPhotosUploaded }: PhotoUploaderProps) {
  const [isDragging, setIsDragging] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [progress, setProgress] = useState({ current: 0, total: 0 });
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFiles = async (files: FileList) => {
    const imageFiles = Array.from(files).filter(file => file.type.startsWith('image/'));

    if (imageFiles.length === 0) {
      alert('请选择图片文件');
      return;
    }

    setIsProcessing(true);
    setProgress({ current: 0, total: imageFiles.length });

    const photos: Photo[] = [];
    for (let i = 0; i < imageFiles.length; i++) {
      const photo = await extractPhotoData(imageFiles[i]);
      photos.push(photo);
      setProgress({ current: i + 1, total: imageFiles.length });
    }

    setIsProcessing(false);
    onPhotosUploaded(photos);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    handleFiles(e.dataTransfer.files);
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      handleFiles(e.target.files);
    }
  };

  return (
    <div className="w-full max-w-4xl mx-auto p-6">
      <div
        onClick={handleClick}
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        className={`
          border-4 border-dashed rounded-xl p-16 text-center cursor-pointer
          transition-all duration-300 ease-in-out
          ${isDragging
            ? 'border-blue-500 bg-blue-50 scale-105'
            : 'border-gray-300 hover:border-blue-400 hover:bg-gray-50'
          }
          ${isProcessing ? 'pointer-events-none opacity-50' : ''}
        `}
      >
        <input
          ref={fileInputRef}
          type="file"
          multiple
          accept="image/*"
          onChange={handleFileChange}
          className="hidden"
        />

        {isProcessing ? (
          <div className="flex flex-col items-center gap-4">
            <Loader2 className="w-16 h-16 text-blue-500 animate-spin" />
            <div className="text-lg font-semibold text-gray-700">
              正在处理照片... {progress.current} / {progress.total}
            </div>
            <div className="w-64 h-2 bg-gray-200 rounded-full overflow-hidden">
              <div
                className="h-full bg-blue-500 transition-all duration-300"
                style={{ width: `${(progress.current / progress.total) * 100}%` }}
              />
            </div>
          </div>
        ) : (
          <div className="flex flex-col items-center gap-4">
            <Upload className="w-16 h-16 text-gray-400" />
            <div className="text-xl font-semibold text-gray-700">
              拖拽照片到这里，或点击选择文件
            </div>
            <div className="text-sm text-gray-500">
              支持批量上传，支持 JPG、PNG 等格式
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
