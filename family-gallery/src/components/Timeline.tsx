import type { PhotoGroup } from '../types';
import { Calendar, MapPin, Camera } from 'lucide-react';

interface TimelineProps {
  groups: PhotoGroup[];
  onGenerateStory: (group: PhotoGroup) => void;
}

const MONTHS = [
  '一月', '二月', '三月', '四月', '五月', '六月',
  '七月', '八月', '九月', '十月', '十一月', '十二月'
];

export default function Timeline({ groups, onGenerateStory }: TimelineProps) {
  return (
    <div className="w-full max-w-6xl mx-auto p-6">
      <h2 className="text-4xl font-bold text-center mb-12 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
        家庭历史时间线
      </h2>

      <div className="relative">
        {/* 时间线中轴 */}
        <div className="absolute left-1/2 transform -translate-x-1/2 h-full w-1 bg-gradient-to-b from-blue-500 to-purple-500" />

        {groups.map((group, index) => (
          <div
            key={`${group.year}-${group.month}`}
            className={`relative mb-16 ${
              index % 2 === 0 ? 'pr-1/2 text-right' : 'pl-1/2 text-left'
            }`}
          >
            {/* 时间点 */}
            <div className="absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2 top-0">
              <div className="w-6 h-6 bg-white border-4 border-blue-500 rounded-full shadow-lg" />
            </div>

            <div
              className={`bg-white rounded-xl shadow-xl p-6 ${
                index % 2 === 0 ? 'mr-12' : 'ml-12'
              }`}
            >
              {/* 标题 */}
              <div className="flex items-center gap-2 mb-4">
                <Calendar className="w-5 h-5 text-blue-500" />
                <h3 className="text-2xl font-bold text-gray-800">
                  {group.year} 年 {MONTHS[group.month]}
                </h3>
              </div>

              {/* 照片网格 */}
              <div className="grid grid-cols-3 gap-2 mb-4">
                {group.photos.slice(0, 6).map((photo) => (
                  <div
                    key={photo.id}
                    className="relative aspect-square rounded-lg overflow-hidden group"
                  >
                    <img
                      src={photo.url}
                      alt=""
                      className="w-full h-full object-cover transition-transform duration-300 group-hover:scale-110"
                    />
                    {photo.exifData?.location && (
                      <div className="absolute top-2 right-2 bg-black bg-opacity-50 text-white p-1 rounded">
                        <MapPin className="w-4 h-4" />
                      </div>
                    )}
                  </div>
                ))}
              </div>

              {group.photos.length > 6 && (
                <div className="text-sm text-gray-500 mb-3">
                  还有 {group.photos.length - 6} 张照片...
                </div>
              )}

              {/* 照片信息 */}
              <div className="flex items-center gap-4 text-sm text-gray-600 mb-4">
                <div className="flex items-center gap-1">
                  <Camera className="w-4 h-4" />
                  <span>{group.photos.length} 张照片</span>
                </div>
                {group.photos[0]?.exifData?.camera && (
                  <div className="text-gray-500">
                    {group.photos[0].exifData.camera}
                  </div>
                )}
              </div>

              {/* AI 故事 */}
              {group.story ? (
                <div className="bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg p-4 mt-4">
                  <h4 className="font-semibold text-gray-800 mb-2">✨ AI 生成的故事</h4>
                  <p className="text-gray-700 leading-relaxed whitespace-pre-wrap">
                    {group.story}
                  </p>
                </div>
              ) : (
                <button
                  onClick={() => onGenerateStory(group)}
                  className="w-full mt-4 bg-gradient-to-r from-blue-500 to-purple-500 text-white py-3 rounded-lg font-semibold hover:shadow-lg transition-all duration-300 transform hover:scale-105"
                >
                  🤖 生成这段时期的故事
                </button>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
