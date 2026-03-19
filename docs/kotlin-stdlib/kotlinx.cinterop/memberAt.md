

# memberAt

Returns the member of this CStructVar which is located by given offset in bytes.

```kotlin
inline fun <T : CPointed> CStructVar.memberAt(offset: Long): T(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.*

/** Simple C struct representation: struct Point { int x; int y; } */
class Point(ptr: CPointer<CPointed>) : CStructVar(ptr) {
    var x: CInt by memberAt(0)   // offset 0
    var y: CInt by memberAt(4)   // offset 4
}

fun main() {
    // Allocate raw memory for the struct (2 * Int.SIZE_BYTES = 8 bytes)
    val rawPtr = malloc(8).reinterpret<CPointer<CPointed>>()
    val point = Point(rawPtr)

    // Write values directly using memberAt
    point.memberAt<CIntVar>(0).value = 10   // x
    point.memberAt<CIntVar>(4).value = 20   // y

    // Read back the values
    println("x = ${point.x}, y = ${point.y}")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/member-at.html)

    