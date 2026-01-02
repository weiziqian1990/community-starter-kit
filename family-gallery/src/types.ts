export interface Photo {
  id: string;
  file: File;
  url: string;
  timestamp: Date;
  exifData?: {
    dateTaken?: Date;
    camera?: string;
    location?: {
      latitude?: number;
      longitude?: number;
    };
  };
}

export interface PhotoGroup {
  year: number;
  month: number;
  photos: Photo[];
  story?: string;
}
