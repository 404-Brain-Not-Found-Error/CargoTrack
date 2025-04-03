import Image from "next/image";
import logo from "../icons/Cargo.png";
import Link from "next/link";

export function MainLoginHeader() {
  return (
    <header className="flex h-[80px] items-center justify-between px-8 shadow-md bg-white fixed w-full top-0 z-50">
      <div className="flex items-center">
        <Image src={logo} alt="Logo" width={50} height={50} priority />
        <div className="w-px h-8 bg-slate-300 mx-4"></div>
        <div className="text-xl font-bold tracking-wide text-slate-900 hover:text-blue-700 transition-colors duration-300">
          <Link href="/about">About</Link>
        </div>
      </div>
    </header>
  );
}
