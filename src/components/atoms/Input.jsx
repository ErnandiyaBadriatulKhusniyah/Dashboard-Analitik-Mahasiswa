import PropTypes from 'prop-types';

const inputStyles = {
    padding: '10px 15px',
    fontSize: '16px',
    width: '100%',
    boxSizing: 'border-box',
};

const labelStyles = {
    display: 'block',
    marginBottom: '5px',
    fontSize: '14px',
    color: '#333',
};

const errorStyles = {
    color: 'red',
    fontSize: '12px',
    marginTop: '5px',
};

const Input = ({
    id,
    label,
    type = 'text',
    value,
    onChange,
    placeholder,
    disabled = false,
    readOnly = false,
    error,
    className,
    style,
    ...restProps
}) => {
    return (
        <div style={style}>
            {label && (
                <label htmlFor={id} style={labelStyles}>
                    {label}
                </label>
            )}
            <input
                id={id}
                type={type}
                value={value}
                onChange={onChange}
                placeholder={placeholder}
                disabled={disabled}
                readOnly={readOnly}
                style={inputStyles}
                className={className}
                {...restProps}
            />
            {error && <p style={errorStyles}>{error}</p>}
        </div>
    );
};

// 3. Definisikan PropTypes untuk validasi props
Input.propTypes = {
    id: PropTypes.string.isRequired,
    label: PropTypes.string,
    type: PropTypes.string,
    value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
    onChange: PropTypes.func.isRequired,
    placeholder: PropTypes.string,
    disabled: PropTypes.bool,
    readOnly: PropTypes.bool,
    error: PropTypes.string,
    className: PropTypes.string,
    style: PropTypes.object,
};

// 4. Definisikan Default Props
Input.defaultProps = {
    type: 'text',
    disabled: false,
    readOnly: false,
};

export default Input;