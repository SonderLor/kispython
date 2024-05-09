from struct import unpack_from, calcsize


class Types:
    float = 'f'
    char = 's'
    int8 = 'b'
    uint16 = 'H'
    uint32 = 'I'
    uint8 = 'B'
    int16 = 'h'
    int32 = 'i'
    int64 = 'q'
    uint64 = 'Q'
    double = 'd'


class BinaryReader:
    def __init__(self, data, offset, order='>'):
        self.data = data
        self.offset = offset
        self.order = order

    def jump_to(self, offset):
        reader = BinaryReader(self.data, offset, self.order)
        return reader

    def read(self, frmt):
        data = unpack_from(self.order + frmt, self.data, self.offset)
        self.offset += calcsize(frmt)
        return data[0]


def read_a(reader):
    a1 = reader.read(Types.double)
    a2 = reader.read(Types.uint64)
    a3 = reader.read(Types.int32)
    b_offset = reader.read(Types.uint32)
    b_reader = reader.jump_to(b_offset)
    a4 = read_b(b_reader)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}


def read_b(reader):
    b1 = reader.read(Types.float)
    b2_size = reader.read(Types.uint16)
    b2_offset = reader.read(Types.uint32)
    b2_reader = reader.jump_to(b2_offset)
    b2 = [read_c(reader.jump_to(b2_reader.read(Types.uint32)))
          for _ in range(b2_size)]
    e_offset = reader.read(Types.uint16)
    e_reader = reader.jump_to(e_offset)
    b3 = read_e(e_reader)
    b4 = read_g(reader)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}


def read_c(reader):
    c1 = reader.read(Types.uint64)
    c2 = read_d(reader)
    return {'C1': c1, 'C2': c2}


def read_d(reader):
    d1 = reader.read(Types.float)
    d2 = reader.read(Types.int32)
    d3 = reader.read(Types.uint32)
    return {'D1': d1, 'D2': d2, 'D3': d3}


def read_e(reader):
    e1 = reader.read(Types.float)
    e2_size = reader.read(Types.uint32)
    e2_offset = reader.read(Types.uint16)
    e2_reader = reader.jump_to(e2_offset)
    e2 = [e2_reader.read(Types.uint32) for _ in range(e2_size)]
    e3 = read_f(reader)
    e4 = reader.read(Types.uint8)
    e5_size = reader.read(Types.uint32)
    e5_offset = reader.read(Types.uint16)
    e5_reader = reader.jump_to(e5_offset)
    e5 = [e5_reader.read(Types.int32) for _ in range(e5_size)]
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4, 'E5': e5}


def read_f(reader):
    f1 = reader.read(Types.int32)
    f2_size = reader.read(Types.uint16)
    f2_offset = reader.read(Types.uint16)
    f2_reader = reader.jump_to(f2_offset)
    f2 = [f2_reader.read(Types.int8) for _ in range(f2_size)]
    f3 = reader.read(Types.int32)
    f4 = reader.read(Types.int16)
    return {'F1': f1, 'F2': f2, 'F3': f3, 'F4': f4}


def read_g(reader):
    g1 = reader.read(Types.int32)
    g2_size = reader.read(Types.uint32)
    g2_offset = reader.read(Types.uint32)
    g2_reader = reader.jump_to(g2_offset)
    g2 = [g2_reader.read(Types.int16) for _ in range(g2_size)]
    g3 = reader.read(Types.int32)
    g4 = reader.read(Types.int8)
    g5 = reader.read(Types.uint16)
    g6 = reader.read(Types.int8)
    g7 = reader.read(Types.int64)
    return {'G1': g1, 'G2': g2, 'G3': g3, 'G4': g4,
            'G5': g5, 'G6': g6, 'G7': g7}


def main(data):
    return read_a(BinaryReader(data, 3))


print(main((b'PBX?\xd5\xd7>BE\xeeX\x93\xd5\x0eyQ\xd6\xe3\xba\x0e4\x8e\r\x00'
            b'\x00\x00\x9c\xb3\xd57\xf7\xd1\xe2k`?{\rh\xd1\x8c\x17Is\x11\x92\xce\xfe'
            b';2\xf0\\\xb7*\x07\xbf}B\xee7\xf4\x00@"\x03=\xd5\x00\x00\x00\x1b\x00'
            b'\x00\x00/\xbd\xab\xea\xa4\x87\x10\xcf|\xff_\x03HQ\x80%_K\x13\xd7h_:\x0cP\x01'
            b"\x0c\xb8Ot\x9b\x8b'\xffd>\xaf\xec\x1e\x00\x00\x00\x02\x00K\xd2v\x001\x00"
            b'\x06\x00Sb\x05QpZJb\x00\x00\x00\x05\x00Y\xea\xd0\xd5J-\xdb\xc3\x8a\xd0:X|'
            b'\xef(\xcd\x8f?N\xbb\x13\x00\x02\x00\x00\x00C\x00mX\x9f\xe0\x9d'
            b'\x00\x00\x00\x08\x00\x00\x00\x8c\xe5\xcd\xd6\xf2\xa1\x1f2\x1d.\xbb\xe9\x0b'
            b'\xde0\xa8\xa0')))
