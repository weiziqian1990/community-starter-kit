import { useState } from 'react';
import { Image, Settings, Sparkles } from 'lucide-react';
import PhotoUploader from './components/PhotoUploader';
import Timeline from './components/Timeline';
import type { Photo, PhotoGroup } from './types';
import { groupPhotosByMonth } from './utils/exifExtractor';
import { generateStory } from './utils/storyGenerator';

function App() {
  const [photos, setPhotos] = useState<Photo[]>([]);
  const [groups, setGroups] = useState<PhotoGroup[]>([]);
  const [apiKey, setApiKey] = useState('');
  const [showSettings, setShowSettings] = useState(false);
  const [isGenerating, setIsGenerating] = useState(false);

  const handlePhotosUploaded = (newPhotos: Photo[]) => {
    const allPhotos = [...photos, ...newPhotos];
    setPhotos(allPhotos);
    const photoGroups = groupPhotosByMonth(allPhotos);
    setGroups(photoGroups);
  };

  const handleGenerateStory = async (group: PhotoGroup) => {
    if (!apiKey) {
      alert('请先在设置中配置 Anthropic API Key');
      setShowSettings(true);
      return;
    }

    setIsGenerating(true);
    try {
      const story = await generateStory(group, apiKey);
      setGroups(prevGroups =>
        prevGroups.map(g =>
          g.year === group.year && g.month === group.month
            ? { ...g, story }
            : g
        )
      );
    } catch (error) {
      console.error('Error generating story:', error);
      alert('生成故事时出错，请检查 API Key 是否正确');
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      {/* 顶部导航 */}
      <nav className="bg-white shadow-md sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Image className="w-8 h-8 text-blue-600" />
            <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
              家庭历史展览馆
            </h1>
          </div>
          <div className="flex items-center gap-4">
            {photos.length > 0 && (
              <div className="text-sm text-gray-600">
                已上传 {photos.length} 张照片
              </div>
            )}
            <button
              onClick={() => setShowSettings(!showSettings)}
              className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <Settings className="w-6 h-6 text-gray-600" />
            </button>
          </div>
        </div>
      </nav>

      {/* 设置面板 */}
      {showSettings && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-xl p-6 max-w-md w-full mx-4 shadow-2xl">
            <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-purple-600" />
              AI 设置
            </h2>
            <div className="mb-4">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Anthropic API Key
              </label>
              <input
                type="password"
                value={apiKey}
                onChange={(e) => setApiKey(e.target.value)}
                placeholder="sk-ant-..."
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
              <p className="text-xs text-gray-500 mt-2">
                在 <a href="https://console.anthropic.com/" target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">Anthropic Console</a> 获取 API Key
              </p>
            </div>
            <div className="flex gap-2">
              <button
                onClick={() => setShowSettings(false)}
                className="flex-1 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors"
              >
                关闭
              </button>
              <button
                onClick={() => {
                  if (apiKey) {
                    localStorage.setItem('anthropic_api_key', apiKey);
                    alert('API Key 已保存');
                    setShowSettings(false);
                  }
                }}
                className="flex-1 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
              >
                保存
              </button>
            </div>
          </div>
        </div>
      )}

      {/* 加载提示 */}
      {isGenerating && (
        <div className="fixed top-20 right-4 bg-blue-600 text-white px-6 py-3 rounded-lg shadow-lg flex items-center gap-2 z-50">
          <div className="animate-spin rounded-full h-4 w-4 border-2 border-white border-t-transparent" />
          正在生成故事...
        </div>
      )}

      {/* 主内容 */}
      <main className="py-8">
        {photos.length === 0 ? (
          <div className="max-w-4xl mx-auto text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-800 mb-4">
              欢迎来到您的家庭历史展览馆
            </h2>
            <p className="text-gray-600 mb-8">
              上传您的照片，让 AI 帮您整理成时间线，并生成温馨的家庭故事
            </p>
            <PhotoUploader onPhotosUploaded={handlePhotosUploaded} />
          </div>
        ) : (
          <>
            <div className="mb-8">
              <PhotoUploader onPhotosUploaded={handlePhotosUploaded} />
            </div>
            <Timeline groups={groups} onGenerateStory={handleGenerateStory} />
          </>
        )}
      </main>

      {/* 页脚 */}
      <footer className="bg-white border-t border-gray-200 mt-16 py-6">
        <div className="max-w-7xl mx-auto px-4 text-center text-gray-600 text-sm">
          <p>使用 React + TypeScript + Vite 构建</p>
          <p className="mt-1">由 Claude AI 提供智能故事生成</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
