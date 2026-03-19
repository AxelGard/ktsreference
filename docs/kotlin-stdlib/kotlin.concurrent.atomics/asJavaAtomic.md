

# asJavaAtomic

Casts the given AtomicInt instance to java.util.concurrent.atomic.AtomicInteger.

```kotlin
@ExperimentalAtomicApifun AtomicInt.asJavaAtomic(): AtomicInteger(source)
```

```kotlin
import kotlin.concurrent.atomics.*
import java.util.concurrent.atomic.AtomicInteger

fun main() {
    @OptIn(ExperimentalAtomicApi::class)
    val atomicInt = atomic(0)

    // Convert the Kotlin AtomicInt to a Java AtomicInteger
    val javaAtomic: AtomicInteger = atomicInt.asJavaAtomic()

    // Use the Java AtomicInteger API
    javaAtomic.incrementAndGet()
    println(javaAtomic.get())   // Prints: 1
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/as-java-atomic.html)

    