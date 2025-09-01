"use client";

import { useState, useEffect, useRef } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { 
  Select, 
  SelectContent, 
  SelectItem, 
  SelectTrigger, 
  SelectValue 
} from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";
import { 
  Camera, 
  MapPin, 
  Clock, 
  Wifi, 
  WifiOff, 
  CheckCircle,
  ChevronRight,
  ChevronLeft,
  Zap,
  ZapOff,
  Image,
  RotateCcw
} from "lucide-react";

const MarineGuardian = () => {
  // App state management
  const [currentScreen, setCurrentScreen] = useState<"splash" | "onboarding" | "capture" | "form" | "success">("splash");
  const [onboardingStep, setOnboardingStep] = useState(0);
  const [cameraPermission, setCameraPermission] = useState<boolean | null>(null);
  const [locationPermission, setLocationPermission] = useState<boolean | null>(null);
  const [flashEnabled, setFlashEnabled] = useState(false);
  const [gpsStatus, setGpsStatus] = useState<"searching" | "locked" | "error">("searching");
  const [capturedImage, setCapturedImage] = useState<string | null>(null);
  const [location, setLocation] = useState<{lat: number, lng: number} | null>(null);
  const [timestamp, setTimestamp] = useState<string>("");
  const [organismType, setOrganismType] = useState<string>("");
  const [organismCondition, setOrganismCondition] = useState<string>("");
  const [notes, setNotes] = useState<string>("");
  const fileInputRef = useRef<HTMLInputElement>(null);

  // Mock onboarding screens focused on Bay of Bengal
  const onboardingScreens = [
    {
      title: "Protect Horseshoe Crabs",
      description: "Report sightings along the Bay of Bengal to support conservation",
      icon: "鲎"
    },
    {
      title: "Easy Reporting",
      description: "Capture or upload photos of horseshoe crabs and marine life",
      icon: "📸"
    },
    {
      title: "Bay of Bengal Conservation",
      description: "Your reports help protect marine biodiversity in our region",
      icon: "🌊"
    }
  ];

  // Updated organism types for Bay of Bengal region
  const organismTypes = [
    "Horseshoe Crab",
    "Shellfish",
    "Shells",
    "Crustaceans",
    "Mollusks",
    "Unknown Organism",
    "Other Marine Life"
  ];

  // Organism conditions
  const organismConditions = [
    "Healthy",
    "Injured",
    "In Distress",
    "Deceased",
    "Unknown"
  ];

  // Simulate splash screen timeout
  useEffect(() => {
    if (currentScreen === "splash") {
      const timer = setTimeout(() => {
        setCurrentScreen("onboarding");
      }, 2000);
      return () => clearTimeout(timer);
    }
  }, [currentScreen]);

  // Simulate GPS acquisition
  useEffect(() => {
    if (currentScreen === "capture") {
      const timer = setTimeout(() => {
        setGpsStatus("locked");
        setLocation({
          lat: 12.8905, // Approximate Bay of Bengal coordinates
          lng: 80.2307
        });
      }, 3000);
      return () => clearTimeout(timer);
    }
  }, [currentScreen]);

  // Handle camera capture
  const handleCapture = () => {
    // In a real app, this would capture an image from the camera
    setCapturedImage("https://placehold.co/400x600/0066cc/ffffff?text=Horseshoe+Crab");
    setTimestamp(new Date().toLocaleString());
    setCurrentScreen("form");
  };

  // Handle gallery upload
  const handleGalleryUpload = () => {
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  };

  // Handle file selection
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0];
      const reader = new FileReader();
      
      reader.onload = (event) => {
        if (event.target?.result) {
          setCapturedImage(event.target.result as string);
          setTimestamp(new Date().toLocaleString());
          setCurrentScreen("form");
        }
      };
      
      reader.readAsDataURL(file);
    }
  };

  // Handle form submission
  const handleSubmit = () => {
    // In a real app, this would submit to a backend
    setCurrentScreen("success");
  };

  // Handle permission requests
  const requestCameraPermission = () => {
    // Simulate permission request
    setCameraPermission(true);
  };

  const requestLocationPermission = () => {
    // Simulate permission request
    setLocationPermission(true);
  };

  // Render splash screen
  if (currentScreen === "splash") {
    return (
      <div className="flex h-screen w-full items-center justify-center bg-blue-50">
        <div className="text-center">
          <div className="mx-auto mb-4 flex h-24 w-24 items-center justify-center rounded-full bg-blue-500">
            <MapPin className="h-12 w-12 text-white" />
          </div>
          <h1 className="text-3xl font-bold text-blue-800">Marine Guardian</h1>
          <p className="mt-2 text-blue-600">Bay of Bengal Conservation</p>
        </div>
      </div>
    );
  }

  // Render onboarding screens
  if (currentScreen === "onboarding") {
    return (
      <div className="flex h-screen flex-col bg-blue-50 p-6">
        <div className="flex flex-1 flex-col items-center justify-center">
          <div className="mb-8 text-6xl">{onboardingScreens[onboardingStep].icon}</div>
          <h2 className="mb-4 text-2xl font-bold text-blue-800">
            {onboardingScreens[onboardingStep].title}
          </h2>
          <p className="text-center text-lg text-blue-600">
            {onboardingScreens[onboardingStep].description}
          </p>
        </div>

        <div className="mb-8 flex justify-center">
          <div className="flex space-x-2">
            {onboardingScreens.map((_, index) => (
              <div
                key={index}
                className={`h-2 w-2 rounded-full ${
                  index === onboardingStep ? "bg-blue-500" : "bg-blue-200"
                }`}
              />
            ))}
          </div>
        </div>

        <div className="flex justify-between">
          {onboardingStep > 0 ? (
            <Button
              variant="outline"
              onClick={() => setOnboardingStep(onboardingStep - 1)}
            >
              <ChevronLeft className="mr-2 h-4 w-4" />
              Back
            </Button>
          ) : (
            <div></div>
          )}

          {onboardingStep < onboardingScreens.length - 1 ? (
            <Button onClick={() => setOnboardingStep(onboardingStep + 1)}>
              Next
              <ChevronRight className="ml-2 h-4 w-4" />
            </Button>
          ) : (
            <Button onClick={() => setCurrentScreen("capture")}>
              Get Started
              <ChevronRight className="ml-2 h-4 w-4" />
            </Button>
          )}
        </div>

        {/* Permission requests */}
        {onboardingStep === onboardingScreens.length - 1 && (
          <Card className="mt-6">
            <CardHeader>
              <CardTitle className="text-lg">Permissions Required</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <p className="font-medium">Camera Access</p>
                  <p className="text-sm text-muted-foreground">
                    To capture horseshoe crab sightings
                  </p>
                </div>
                {cameraPermission === null ? (
                  <Button onClick={requestCameraPermission} size="sm">
                    Allow
                  </Button>
                ) : (
                  <span className="text-green-500">Granted</span>
                )}
              </div>

              <div className="flex items-center justify-between">
                <div>
                  <p className="font-medium">Location Access</p>
                  <p className="text-sm text-muted-foreground">
                    To record sighting locations in Bay of Bengal
                  </p>
                </div>
                {locationPermission === null ? (
                  <Button onClick={requestLocationPermission} size="sm">
                    Allow
                  </Button>
                ) : (
                  <span className="text-green-500">Granted</span>
                )}
              </div>
            </CardContent>
          </Card>
        )}
      </div>
    );
  }

  // Render capture screen
  if (currentScreen === "capture") {
    return (
      <div className="flex h-screen flex-col bg-black">
        {/* Camera view placeholder */}
        <div className="relative flex-1">
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="h-full w-full bg-gradient-to-b from-blue-900 to-blue-700 opacity-80" />
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="text-center">
                <Camera className="mx-auto h-16 w-16 text-white opacity-70" />
                <p className="mt-2 text-white">Camera View</p>
                <p className="mt-1 text-sm text-white/80">Point at horseshoe crabs</p>
              </div>
            </div>
          </div>

          {/* GPS status indicator */}
          <div className="absolute left-4 top-4 flex items-center rounded-full bg-black/50 px-3 py-1 text-white">
            {gpsStatus === "searching" ? (
              <>
                <WifiOff className="mr-2 h-4 w-4" />
                <span>Acquiring location...</span>
              </>
            ) : gpsStatus === "locked" ? (
              <>
                <Wifi className="mr-2 h-4 w-4" />
                <span>Bay of Bengal location</span>
              </>
            ) : (
              <>
                <WifiOff className="mr-2 h-4 w-4" />
                <span>Location error</span>
              </>
            )}
          </div>

          {/* Flash toggle */}
          <Button
            variant="secondary"
            size="icon"
            className="absolute right-4 top-4 rounded-full"
            onClick={() => setFlashEnabled(!flashEnabled)}
          >
            {flashEnabled ? (
              <Zap className="h-5 w-5" />
            ) : (
              <ZapOff className="h-5 w-5" />
            )}
          </Button>
        </div>

        {/* Action buttons */}
        <div className="flex items-center justify-center gap-6 bg-black p-6">
          <Button
            variant="secondary"
            size="icon"
            className="h-14 w-14 rounded-full"
            onClick={handleGalleryUpload}
          >
            <Image className="h-6 w-6" />
          </Button>
          
          <Button
            className="h-20 w-20 rounded-full border-4 border-white bg-white p-0 hover:bg-gray-100"
            onClick={handleCapture}
          >
            <Camera className="h-10 w-10 text-black" />
          </Button>
          
          <Button
            variant="secondary"
            size="icon"
            className="h-14 w-14 rounded-full"
            onClick={() => setFlashEnabled(!flashEnabled)}
          >
            {flashEnabled ? (
              <Zap className="h-6 w-6" />
            ) : (
              <ZapOff className="h-6 w-6" />
            )}
          </Button>
        </div>

        {/* Hidden file input for gallery upload */}
        <input
          type="file"
          ref={fileInputRef}
          className="hidden"
          accept="image/*"
          onChange={handleFileChange}
        />
      </div>
    );
  }

  // Render form screen
  if (currentScreen === "form") {
    return (
      <div className="flex h-screen flex-col bg-blue-50 p-4">
        <div className="mb-4 flex items-center justify-between">
          <h1 className="text-2xl font-bold text-blue-800">Report Sighting</h1>
          <div className="flex gap-2">
            <Button
              variant="outline"
              size="sm"
              onClick={handleGalleryUpload}
            >
              <Image className="mr-1 h-4 w-4" />
              Change
            </Button>
            <Button
              variant="outline"
              size="sm"
              onClick={() => setCurrentScreen("capture")}
            >
              <RotateCcw className="mr-1 h-4 w-4" />
              Retake
            </Button>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto">
          <Card className="mb-4">
            <CardContent className="p-0">
              <div className="bg-gray-200">
                {capturedImage ? (
                  <img
                    src={capturedImage}
                    alt="Captured sighting"
                    className="h-64 w-full object-cover"
                  />
                ) : (
                  <div className="flex h-64 items-center justify-center">
                    <Camera className="h-12 w-12 text-gray-400" />
                  </div>
                )}
              </div>
            </CardContent>
          </Card>

          <Card className="mb-4">
            <CardHeader>
              <CardTitle className="text-lg">Sighting Details</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="flex items-center">
                <MapPin className="mr-2 h-5 w-5 text-blue-500" />
                <div>
                  <p className="font-medium">Location</p>
                  {location ? (
                    <p className="text-sm text-muted-foreground">
                      {location.lat.toFixed(4)}, {location.lng.toFixed(4)} (Bay of Bengal)
                    </p>
                  ) : (
                    <p className="text-sm text-muted-foreground">
                      Location not available
                    </p>
                  )}
                </div>
              </div>

              <div className="flex items-center">
                <Clock className="mr-2 h-5 w-5 text-blue-500" />
                <div>
                  <p className="font-medium">Timestamp</p>
                  <p className="text-sm text-muted-foreground">{timestamp}</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="mb-4">
            <CardHeader>
              <CardTitle className="text-lg">Organism Information</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <Label htmlFor="organism-type">Organism Type *</Label>
                <Select value={organismType} onValueChange={setOrganismType} required>
                  <SelectTrigger id="organism-type">
                    <SelectValue placeholder="Select organism type" />
                  </SelectTrigger>
                  <SelectContent>
                    {organismTypes.map((type) => (
                      <SelectItem key={type} value={type}>
                        {type}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              <div>
                <Label htmlFor="organism-condition">Condition</Label>
                <Select
                  value={organismCondition}
                  onValueChange={setOrganismCondition}
                >
                  <SelectTrigger id="organism-condition">
                    <SelectValue placeholder="Select condition (optional)" />
                  </SelectTrigger>
                  <SelectContent>
                    {organismConditions.map((condition) => (
                      <SelectItem key={condition} value={condition}>
                        {condition}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              <div>
                <Label htmlFor="notes">Additional Notes</Label>
                <Textarea
                  id="notes"
                  placeholder="Describe the sighting, behavior, or environment..."
                  value={notes}
                  onChange={(e) => setNotes(e.target.value)}
                  rows={3}
                />
              </div>
            </CardContent>
          </Card>
        </div>

        <Button
          className="mt-4 w-full bg-blue-600 hover:bg-blue-700"
          onClick={handleSubmit}
          disabled={!organismType}
        >
          Submit Report
        </Button>
      </div>
    );
  }

  // Render success screen
  if (currentScreen === "success") {
    return (
      <div className="flex h-screen flex-col items-center justify-center bg-blue-50 p-6">
        <div className="mb-6 rounded-full bg-green-100 p-4">
          <CheckCircle className="h-16 w-16 text-green-500" />
        </div>
        <h1 className="mb-2 text-3xl font-bold text-green-700">Report Submitted!</h1>
        <p className="mb-2 text-center text-lg text-green-600">
          Thank you for protecting horseshoe crabs in the Bay of Bengal
        </p>
        <p className="mb-8 text-center text-muted-foreground">
          Your report helps scientists track populations and protect habitats
        </p>
        <Button
          className="w-full bg-blue-600 hover:bg-blue-700"
          onClick={() => {
            // Reset form and return to capture screen
            setCapturedImage(null);
            setOrganismType("");
            setOrganismCondition("");
            setNotes("");
            setCurrentScreen("capture");
          }}
        >
          Report Another Sighting
        </Button>
      </div>
    );
  }

  return null;
};

export default MarineGuardian;