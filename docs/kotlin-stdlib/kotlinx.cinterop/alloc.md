

# alloc

Allocates variable of given type.

```kotlin
inline fun <T : CVariable> NativePlacement.alloc(): T(source)
```

```kotlin
import kotlinx.cinterop.*

fun main() {
    memScoped {
        // Allocate a CInt variable on the stack
        val intVar = alloc<IntVar>()

        // Initialise the variable
        intVar.value = 42

        // Use the variable
        println("CInt value: ${intVar.value}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/alloc.html)

    