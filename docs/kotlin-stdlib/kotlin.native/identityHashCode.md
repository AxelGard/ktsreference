

# identityHashCode

Compute stable wrt potential object relocations by the memory manager identity hash code.

```kotlin
@ExperimentalNativeApiexternal fun Any?.identityHashCode(): Int(source)
```

```kotlin
import kotlin.native.identityHashCode
import kotlin.experimental.ExperimentalNativeApi

@OptIn(ExperimentalNativeApi::class)
fun main() {
    val a = "hello"
    val b = "hello"

    println("a.hashCode()        = ${a.hashCode()}")
    println("b.hashCode()        = ${b.hashCode()}")
    println("a.identityHashCode() = ${a.identityHashCode()}")
    println("b.identityHashCode() = ${b.identityHashCode()}")
    println("a === b             = ${a === b}")

    val c = Any()
    val d = Any()
    println("c.identityHashCode() = ${c.identityHashCode()}")
    println("d.identityHashCode() = ${d.identityHashCode()}")

    val nullObj: Any? = null
    println("null.identityHashCode() = ${nullObj.identityHashCode()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/identity-hash-code.html)

    