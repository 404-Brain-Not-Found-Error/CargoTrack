import Image from "next/image";
import logo from "./icons/Cargo.png";

export function Header() {
    return (
      <header className="flex h-[100px] items-center px-8 shadow-xl">
        <Image src={logo} alt="Logo" width={65} height={65} />
        <div className="w-px h-8 bg-slate-200 mx-6"></div>
        <div className="text-2xl font-semibold tracking-wide text-slate-800 hover:text-blue-600 transition-colors">
          CargoTrack
        </div>
      </header>
    );
  }