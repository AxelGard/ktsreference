

# interpretNullablePointed

Performs type cast of the native pointer to given interop type, including null values.

```kotlin
external fun <T : NativePointed> interpretNullablePointed(ptr: NativePtr): T?(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.*

@CStruct("Point")
class Point(rawPtr: NativePtr) : CStructVar(rawPtr) {
    var x: Int
        get() = member<IntVar>(offsetof(Point, "x")).value
        set(value) { member<IntVar>(offsetof(Point, "x")).value = value }
    var y: Int
        get() = member<IntVar>(offsetof(Point, "y")).value
        set(value) { member<IntVar>(offsetof(Point, "y")).value = value }
}

fun main() {
    // Allocate native memory for a Point struct
    val nativePtr = malloc(sizeof<Point>())

    // Interpret the raw pointer as a nullable CPointer<Point>
    val pointPtr: CPointer<Point>? = interpretNullablePointed(nativePtr)

    // Use the pointer if it is not null
    pointPtr?.pointed?.apply {
        x = 42
        y = 99
        println("Point(x=$x, y=$y)")
    }

    // Clean up
    free(nativePtr)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/interpret-nullable-pointed.html)

    