# Eastworld Miner

A specialized Bittensor miner implementation for the Eastworld subnet (SN94), focusing on navigation and SLAM capabilities.

## Overview

The Eastworld Miner is designed to excel in navigation and Simultaneous Localization and Mapping (SLAM) tasks within the Bittensor network. It implements advanced algorithms for:

- Environment mapping and localization
- Path planning and optimization
- Obstacle detection and avoidance
- Multi-agent coordination
- Experience-based learning

## Features

- **Advanced Navigation**: Implements SLAM using GTSAM for accurate environment mapping
- **Intelligent Path Planning**: Uses NetworkX for optimal path finding
- **Learning System**: Incorporates experience replay and pattern learning
- **Memory Management**: Implements both short-term and long-term memory systems
- **Bittensor Integration**: Seamless integration with the Bittensor network

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/eastworld-miner.git
cd eastworld-miner
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
eastworld-miner/
├── src/
│   └── eastworld_miner/
│       ├── core/          # Core miner functionality
│       ├── navigation/    # Navigation and SLAM algorithms
│       ├── memory/        # Memory system implementation
│       └── utils/         # Utility functions
├── tests/                 # Test suite
├── docs/                  # Documentation
└── requirements.txt       # Project dependencies
```

## Development

To run tests:
```bash
pytest
```

To run with coverage:
```bash
pytest --cov=src/eastworld_miner
```

## Documentation

Detailed documentation is available in the `docs/` directory:
- [Development Notes](docs/development_notes.md)
- [API Reference](docs/api.md)
- [Architecture](docs/architecture.md)

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Bittensor](https://bittensor.com/) for the underlying network infrastructure
- [GTSAM](https://gtsam.org/) for SLAM implementation
- [NetworkX](https://networkx.org/) for path planning
- [OpenCV](https://opencv.org/) for computer vision tasks 