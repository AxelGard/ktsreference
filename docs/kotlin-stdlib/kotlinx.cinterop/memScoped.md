

# memScoped

Runs given block providing allocation of memory which will be automatically disposed at the end of this scope.

```kotlin
inline fun <R> memScoped(block: MemScope.() -> R): R(source)
```

```kotlin
import kotlinx.cinterop.*

fun main() {
    memScoped {
        val ptr = alloc<IntVar>()   // allocate an Int on the C heap
        ptr.value = 42              // set the value
        println("Value in C memory: ${ptr.value}")  // read it back
    }   // the allocated memory is automatically freed here
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/mem-scoped.html)

    