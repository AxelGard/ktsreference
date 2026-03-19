

# typeOf

Use sizeOf<T>() or alignOf<T>() instead.

```kotlin
fun <T : CVariable> typeOf(): CVariable.Type(source)
```

```kotlin
import kotlinx.cinterop.*

fun main() {
    // Retrieve the C type information for a CInt
    val intType = typeOf<CIntVar>()
    println("CIntVar type: $intType")

    // Retrieve the C type information for a CDouble
    val doubleType = typeOf<CDoubleVar>()
    println("CDoubleVar type: $doubleType")

    // Allocate memory using the retrieved type
    val ptr = nativeHeap.alloc<CIntVar>()
    ptr.value = 123
    println("Allocated CIntVar value: ${ptr.value}")

    // Free the allocated memory
    nativeHeap.free(ptr)
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/type-of.html)

    