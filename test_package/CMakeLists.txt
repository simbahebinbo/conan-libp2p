CMAKE_MINIMUM_REQUIRED(VERSION 3.12)

PROJECT(demo LANGUAGES CXX VERSION 1.0.0)

set(CMAKE_POSITION_INDEPENDENT_CODE TRUE)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(p2p CONFIG REQUIRED)

add_executable(multiaddress
        multiaddress.cpp
)

target_link_libraries(multiaddress
        p2p::p2p_multiaddress
)
