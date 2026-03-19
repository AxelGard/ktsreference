

# interpretPointed

Returns interpretation of entity with given pointer.

```kotlin
inline fun <T : NativePointed> interpretPointed(ptr: NativePtr): T(source)
```

```kotlin
import kotlinx.cinterop.*

fun main() {
    memScoped {
        // Allocate a C int variable on the heap
        val intPtr: CPointer<CIntVar> = nativeHeap.alloc<CIntVar>()
        intPtr.pointed.value = 42

        // Interpret the raw pointer as a CIntVar using interpretPointed
        val interpreted: CIntVar = interpretPointed(intPtr)

        println("Interpreted value: ${interpreted.value}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/interpret-pointed.html)

    