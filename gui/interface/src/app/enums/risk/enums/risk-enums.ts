'use strict';

export const RiskEnums =
    {
        alarming: [{ label: 'Level A1', value: 'a1' }, { label: 'Level A2', value: 'a2' }, { label: 'Level A3', value: 'a3' }],
        complexity: [{ label: 'Level B1', value: 'b1' }, { label: 'Level B2', value: 'b2' }, { label: 'Level B3', value: 'b3' }],
        managment: [{ label: 'Level M1', value: 'm1' }, { label: 'Level M2', value: 'm2' }, { label: 'Level M3', value: 'm3' }],
        detectorType: [ { label: 'Heat detector', value: 'heat' }, { label: 'Smoke detector', value: 'smoke' } ],
        materials: [
            { label: 'Gypsum', value: 'gypsum' },
            { label: 'Brick', value: 'brick' },
            { label: 'Concrete', value: 'concrete' }
        ],
        buildingType: [
            {   // alpha: 0.0029, 0.012, 0.047, 0.188
                label: 'Hotel',
                value: 'hotel',
                type: 'c1',
                alphaMod: 0.047,
                hrrpua: 500, // pokazac w ustawieniach
                maxHrr: [100, 500],
                evacRoomDensity: 1, // z bs 9999
                evacCorridorDensity: 1, // z bs 9999
                evacStaircaseDensity: 1, // z bs 9999
                evacHallDensity: 1, // z bs 9999
            },
            {
                label: 'Office (closed plan)',
                value: 'office1',
                type: 'b',
                alphaMod: 0.012,
                hrrpua: 500, // pokazac w ustawieniach
                maxHrr: [100, 500],
                evacRoomDensity: 1, // z bs 9999
                evacCorridorDensity: 1, // z bs 9999
                evacStaircaseDensity: 1, // z bs 9999
                evacHallDensity: 1, // z bs 9999
            },
			{
                label: 'Admisitration office',
                value: 'office2',
                type: 'a',
                alphaMod: 0.012,
                hrrpua: 500, // pokazac w ustawieniach
                maxHrr: [100, 500],
                evacRoomDensity: 1, // z bs 9999
                evacCorridorDensity: 1, // z bs 9999
                evacStaircaseDensity: 1, // z bs 9999
                evacHallDensity: 1, // z bs 9999
            },
			{
                label: 'Amusement arcade',
                value: 'arcade',
                type: 'b',
                alphaMod: 0.012,
                hrrpua: 500, // pokazac w ustawieniach
                maxHrr: [100, 500],
                evacRoomDensity: 1, // z bs 9999
                evacCorridorDensity: 1, // z bs 9999
                evacStaircaseDensity: 1, // z bs 9999
                evacHallDensity: 1, // z bs 9999
            },
			{
                label: 'Archive/library',
                value: 'library',
                type: 'b',
                alphaMod: 0.047,
                hrrpua: 500, // pokazac w ustawieniach
                maxHrr: [100, 500],
                evacRoomDensity: 1, // z bs 9999
                evacCorridorDensity: 1, // z bs 9999
                evacStaircaseDensity: 1, // z bs 9999
                evacHallDensity: 1, // z bs 9999
            },
			{
                label: 'Art gallery',
                value: 'gallery',
                type: 'b',
                alphaMod: 0.012,
                hrrpua: 500, // pokazac w ustawieniach
                maxHrr: [100, 500],
                evacRoomDensity: 1, // z bs 9999
                evacCorridorDensity: 1, // z bs 9999
                evacStaircaseDensity: 1, // z bs 9999
                evacHallDensity: 1, // z bs 9999
            },
			{
                label: 'Assembly hall',
                value: 'assembly',
                type: 'b',
                alphaMod: 0.012,
                hrrpua: 500, // pokazac w ustawieniach
                maxHrr: [100, 500],
                evacRoomDensity: 1, // z bs 9999
                evacCorridorDensity: 1, // z bs 9999
                evacStaircaseDensity: 1, // z bs 9999
                evacHallDensity: 1, // z bs 9999
            },
        ],
        preTimes: [
            {
                type: 'a',
                preEvacuationRoomOfFireOrigin: [29.85, 1.48],
                pre: {
                    m1: {
                        b1: { a1: { loc: 29.71, scale: 2.96 }, a2: { loc: 29.71, scale: 2.96 } },
                        b2: { a1: { loc: 29.71, scale: 2.96 }, a2: { loc: 29.71, scale: 2.96 } },
                        b3: { a1: { loc: 59.71, scale: 2.96 }, a2: { loc: 59.71, scale: 2.96 } }
                    },
                    m2: {
                        b1: { a1: { loc: 59.42, scale: 5.92 }, a2: { loc: 59.42, scale: 5.92 } },
                        b2: { a1: { loc: 59.42, scale: 5.92 }, a2: { loc: 59.42, scale: 5.92 } },
                        b3: { a1: { loc: 89.42, scale: 5.92 }, a2: { loc: 89.42, scale: 5.92 } }
                    },
                    m3: {
                        b1: { a1: { loc: 899.42, scale: 5.92 }, a2: { loc: 899.42, scale: 5.92 } },
                        b2: { a1: { loc: 899.42, scale: 5.92 }, a2: { loc: 899.42, scale: 5.92 } },
                        b3: { a1: { loc: 929.42, scale: 5.92 }, a2: { loc: 929.42, scale: 5.92 }, a3: { loc: 929.42, scale: 5.92 } }
                    }
                }
            },
            {
                type: 'b',
                preEvacuationRoomOfFireOrigin: [59.85, 1.48],
                pre: {
                    m1: {
                        b1: { a1: { loc: 29.13, scale: 8.87 }, a2: { loc: 29.13, scale: 8.87 } },
                        b2: { a1: { loc: 59.13, scale: 8.87 }, a2: { loc: 59.13, scale: 8.87 } },
                        b3: { a1: { loc: 89.13, scale: 8.87 }, a2: { loc: 89.13, scale: 8.87 } }
                    },
                    m2: {
                        b1: { a1: { loc: 58.84, scale: 11.83 }, a2: { loc: 58.84, scale: 11.83 } },
                        b2: { a1: { loc: 88.84, scale: 11.83 }, a2: { loc: 88.84, scale: 11.83 } },
                        b3: { a1: { loc: 118.84, scale: 11.83 }, a2: { loc: 118.84, scale: 11.83 } }
                    },
                    m3: {
                        b1: { a1: { loc: 899.42, scale: 5.92 }, a2: { loc: 899.42, scale: 5.92 } },
                        b2: { a1: { loc: 899.42, scale: 5.92 }, a2: { loc: 899.42, scale: 5.92 } },
                        b3: { a1: { loc: 929.42, scale: 5.92 }, a2: { loc: 929.42, scale: 5.92 }, a3: { loc: 929.42, scale: 5.92 } }
                    }
                }
            },
            {
                type: 'c1',
                preEvacuationRoomOfFireOrigin: [59.85, 1.48],
                pre: {
                    m1: {
                        b1: { a1: { loc: 29.71, scale: 2.96 }, a2: { loc: 29.71, scale: 2.96 } },
                        b2: { a1: { loc: 594.22, scale: 59.16 }, a2: { loc: 594.22, scale: 59.16 } },
                        b3: { a1: { loc: 59.71, scale: 2.96 }, a2: { loc: 59.71, scale: 2.96 } }
                    },
                    m2: {
                        b1: { a1: { loc: 299.94, scale: 0.59 }, a2: { loc: 30, scale: 60 } },
                        b2: { a1: { loc: 894.22, scale: 59.16 }, a2: { loc: 894.22, scale: 59.16 } },
                        b3: { a1: { loc: 30, scale: 60 }, a2: { loc: 30, scale: 60 }, a3: { loc: 30, scale: 60 } }
                    },
                    m3: {
                        b1: { a1: { loc: 30, scale: 60 }, a2: { loc: 30, scale: 60 }, a3: { loc: 594.22, scale: 59.16 } },
                        b2: { a1: { loc: 1199.94, scale: 0.59 }, a2: { loc: 1199.94, scale: 0.59 }, a3: { loc: 1199.94, scale: 0.59 } },
                        b3: { a1: { loc: 30, scale: 60 }, a2: { loc: 30, scale: 60 }, a3: { loc: 30, scale: 60 } }
                    }
                }
            },
            {
                type: 'c2',
                preEvacuationRoomOfFireOrigin: [59.85, 1.48],
                pre: {
                    m1: {
                        b1: { a1: { loc: 29.71, scale: 2.96 }, a2: { loc: 29.71, scale: 2.96 } },
                        b2: { a1: { loc: 594.22, scale: 59.16 }, a2: { loc: 594.22, scale: 59.16 } },
                        b3: { a1: { loc: 59.71, scale: 2.96 }, a2: { loc: 59.71, scale: 2.96 } }
                    },
                    m2: {
                        b1: { a1: { loc: 299.94, scale: 0.59 }, a2: { loc: 30, scale: 60 } },
                        b2: { a1: { loc: 894.22, scale: 59.16 }, a2: { loc: 894.22, scale: 59.16 } },
                        b3: { a1: { loc: 30, scale: 60 }, a2: { loc: 30, scale: 60 }, a3: { loc: 30, scale: 60 } }
                    },
                    m3: {
                        b1: { a1: { loc: 30, scale: 60 }, a2: { loc: 30, scale: 60 }, a3: { loc: 594.22, scale: 59.16 } },
                        b2: { a1: { loc: 1199.94, scale: 0.59 }, a2: { loc: 1199.94, scale: 0.59 }, a3: { loc: 1199.94, scale: 0.59 } },
                        b3: { a1: { loc: 30, scale: 60 }, a2: { loc: 30, scale: 60 }, a3: { loc: 30, scale: 60 } }
                    }
                }
            },
            {
                type: 'c3',
                preEvacuationRoomOfFireOrigin: [59.85, 1.48],
                pre: {
                    m1: {
                        b1: { a1: { loc: 29.71, scale: 2.96 }, a2: { loc: 29.71, scale: 2.96 } },
                        b2: { a1: { loc: 594.22, scale: 59.16 }, a2: { loc: 594.22, scale: 59.16 } },
                        b3: { a1: { loc: 59.71, scale: 2.96 }, a2: { loc: 59.71, scale: 2.96 } }
                    },
                    m2: {
                        b1: { a1: { loc: 299.94, scale: 0.59 }, a2: { loc: 30, scale: 60 } },
                        b2: { a1: { loc: 894.22, scale: 59.16 }, a2: { loc: 894.22, scale: 59.16 } },
                        b3: { a1: { loc: 30, scale: 60 }, a2: { loc: 30, scale: 60 }, a3: { loc: 30, scale: 60 } }
                    },
                    m3: {
                        b1: { a1: { loc: 30, scale: 60 }, a2: { loc: 30, scale: 60 }, a3: { loc: 594.22, scale: 59.16 } },
                        b2: { a1: { loc: 1199.94, scale: 0.59 }, a2: { loc: 1199.94, scale: 0.59 }, a3: { loc: 1199.94, scale: 0.59 } },
                        b3: { a1: { loc: 30, scale: 60 }, a2: { loc: 30, scale: 60 }, a3: { loc: 30, scale: 60 } }
                    }
                }
            },
            {
                type: 'd1',
                preEvacuationRoomOfFireOrigin: [59.85, 1.48],
                pre: {
                    m1: {
                        b1: { a1: { loc: 28.84, scale: 11.83 }, a2: { loc: 28.84, scale: 11.83 } },
                        b2: { a1: { loc: 59.13, scale: 8.87 }, a2: { loc: 59.13, scale: 8.87 } },
                        b3: { a1: { loc: 89.13, scale: 8.87 }, a2: { loc: 89.13, scale: 8.87 } }
                    },
                    m2: {
                        b1: { a1: { loc: 58.84, scale: 11.83 }, a2: { loc: 58.84, scale: 11.83 } },
                        b2: { a1: { loc: 894.22, scale: 59.16 }, a2: { loc: 894.22, scale: 59.16 } },
                        b3: { a1: { loc: 30, scale: 60 }, a2: { loc: 30, scale: 60 }, a3: { loc: 30, scale: 60 } }
                    },
                    m3: {
                        b1: { a1: { loc: 899.94, scale: 0.59 }, a2: { loc: 899.94, scale: 0.59 }, a3: { loc: 899.94, scale: 0.59 } },
                        b2: { a1: { loc: 1199.94, scale: 0.59 }, a2: { loc: 1199.94, scale: 0.59 }, a3: { loc: 1199.94, scale: 0.59 } },
                        b3: { a1: { loc: 1259.94, scale: 0.59 }, a2: { loc: 1259.94, scale: 0.59 }, a3: { loc: 1259.94, scale: 0.59 } }
                    }
                }
            },
            {
                type: 'd2',
                preEvacuationRoomOfFireOrigin: [59.85, 1.48],
                pre: {
                    m1: {
                        b2: { a1: { loc: 297.11, scale: 29.56 }, a2: { loc: 297.11, scale: 29.56 } },
                        b3: { a1: { loc: 357.11, scale: 29.58 }, a2: { loc: 357.11, scale: 29.58 } }
                    },
                    m2: {
                        b2: { a1: { loc: 594.22, scale: 59.16 }, a2: { loc: 594.22, scale: 59.16 } },
                        b3: { a1: { loc: 654.22, scale: 59.16 }, a2: { loc: 654.22, scale: 59.16 } }
                    },
                    m3: {
                        b2: { a1: { loc: 594.22, scale: 59.16 }, a2: { loc: 594.22, scale: 59.16 } },
                        b3: { a1: { loc: 654.22, scale: 59.16 }, a2: { loc: 654.22, scale: 59.16 }, a3: { loc: 654.22, scale: 59.16 } }
                    }
                }
            },
            {
                type: 'e',
                preEvacuationRoomOfFireOrigin: [59.85, 1.48],
                pre: {
                    m1: {
                        b3: { a1: { loc: 88.56, scale: 14.79 }, a2: { loc: 88.56, scale: 14.79 } }
                    },
                    m2: {
                        b3: { a1: { loc: 118.27, scale: 17.75 }, a2: { loc: 118.27, scale: 17.75 } }
                    },
                    m3: {
                        b3: { a1: { loc: 899.94, scale: 0.59 }, a2: { loc: 899.94, scale: 0.59 }, a3: { loc: 899.94, scale: 0.59 } }
                    }
                }
            },
        ]
    };