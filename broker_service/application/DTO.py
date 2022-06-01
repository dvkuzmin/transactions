from pydantic import BaseModel, validator


class ClientDTO(BaseModel):
    name: str
    email: str
    psw: str
    psw_repeat: str

    @validator('psw')
    def psw_is_valid(cls, v):
        if len(v) < 5:
            raise ValueError('Password must be 5 or more symbols')
        return v

    @validator("psw_repeat")
    def psw_repeat_is_valid(cls, v, values):
        if 'psw' in values and values['psw'] != v:
            raise ValueError('Password is not matched')
        return v


class ClientLoginDto(BaseModel):
    email: str
    psw: str
