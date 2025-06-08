import Sidebar from "../molecules/Sidebar";

const Layout = ({ className, children }) => {
  return (
    <div className="layout h-full grid grid-cols-[15%_auto] bg-[#2A0E99]">
      <Sidebar />
      <main className={`h-full p-10 ${className}`}>{children}</main>
    </div>
  );
};

export default Layout;
