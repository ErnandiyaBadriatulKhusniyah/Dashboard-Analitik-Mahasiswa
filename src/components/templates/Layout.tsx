const Layout = ({
    className,
    children
}) => {
    return (
        <div className="layout h-full grid grid-cols-[15%_auto] bg-[#2A0E99]">
            <aside className="bg-white h-full p-5">Sidebar</aside>
            <main className={`h-full p-10 ${className}`}>
                {children}
            </main>
        </div>
    )
}

export default Layout;