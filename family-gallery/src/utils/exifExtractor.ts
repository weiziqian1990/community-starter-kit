import exifr from 'exifr';
import type { Photo } from '../types';

export async function extractPhotoData(file: File): Promise<Photo> {
  const url = URL.createObjectURL(file);
  const id = `${file.name}-${Date.now()}`;

  try {
    const exif = await exifr.parse(file, {
      pick: ['DateTimeOriginal', 'CreateDate', 'ModifyDate', 'Make', 'Model', 'latitude', 'longitude']
    });

    const dateTaken = exif?.DateTimeOriginal || exif?.CreateDate || exif?.ModifyDate;
    const timestamp = dateTaken ? new Date(dateTaken) : new Date(file.lastModified);

    return {
      id,
      file,
      url,
      timestamp,
      exifData: {
        dateTaken: dateTaken ? new Date(dateTaken) : undefined,
        camera: exif?.Make && exif?.Model ? `${exif.Make} ${exif.Model}` : undefined,
        location: exif?.latitude && exif?.longitude ? {
          latitude: exif.latitude,
          longitude: exif.longitude,
        } : undefined,
      },
    };
  } catch (error) {
    console.error('Error extracting EXIF data:', error);
    return {
      id,
      file,
      url,
      timestamp: new Date(file.lastModified),
    };
  }
}

export function groupPhotosByMonth(photos: Photo[]) {
  const groups = new Map<string, Photo[]>();

  photos.forEach(photo => {
    const key = `${photo.timestamp.getFullYear()}-${photo.timestamp.getMonth()}`;
    if (!groups.has(key)) {
      groups.set(key, []);
    }
    groups.get(key)!.push(photo);
  });

  return Array.from(groups.entries())
    .map(([key, photos]) => {
      const [year, month] = key.split('-').map(Number);
      return {
        year,
        month,
        photos: photos.sort((a, b) => a.timestamp.getTime() - b.timestamp.getTime()),
      };
    })
    .sort((a, b) => {
      if (a.year !== b.year) return b.year - a.year;
      return b.month - a.month;
    });
}
