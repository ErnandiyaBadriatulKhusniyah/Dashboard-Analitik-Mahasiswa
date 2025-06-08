
const Typography = ({
    children,
    className,
    variantClass
}) => {
    const variantClassesMap = {
        title: "text-4xl font-bold text-gray-900 leading-tight mb-4",
        subtitle: "text-2xl font-semibold text-gray-700 mb-2",
        body: "text-base text-gray-600",
        caption: "text-sm text-gray-500",
    };
    const dynamicVariantClass = variantClassesMap[variantClass] || '';

    const finalClasses = `${dynamicVariantClass} ${className || ''}`.trim();

    let Tag = 'p'; // Default tag
    if (variantClass === 'title') {
        Tag = 'h1';
    } else if (variantClass === 'subtitle') {
        Tag = 'h2';
    }

    return (
        <>
            <Tag className={finalClasses}>{children}</Tag>
        </>
    )
}

export default Typography;