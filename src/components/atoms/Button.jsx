const Button = ({
    btnText,
    disabled = false,
    type = "button",
    className,
    ...restProps
}) => {
    return (
        <>
            <button
                className={className}
                type={type}
                disabled={disabled}
                {...restProps} >
                {btnText}
            </button>
        </>
    )
}

export default Button