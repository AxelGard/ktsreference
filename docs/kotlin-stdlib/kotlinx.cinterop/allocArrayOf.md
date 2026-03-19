

# allocArrayOf

Allocates C array of given values.

```kotlin
inline fun <T : CPointer<*>> NativePlacement.allocArrayOf(vararg elements: T?): CArrayPointer<CPointerVarOf<T>>(source)
```

```kotlin
import kotlinx.cinterop.*

fun main() = memScoped {
    // Allocate two C ints and set their values
    val p1: CPointer<IntVar> = alloc()
    val p2: CPointer<IntVar> = alloc()
    p1.pointed.value = 10
    p2.pointed.value = 20

    // Create a C array that holds the two pointers
    val array: CArrayPointer<CPointerVarOf<IntVar>> = allocArrayOf(p1, p2)

    // Access the values through the array
    println("array[0] = ${array[0]!!.pointed.value}")  // 10
    println("array[1] = ${array[1]!!.pointed.value}")  // 20
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/alloc-array-of.html)

    