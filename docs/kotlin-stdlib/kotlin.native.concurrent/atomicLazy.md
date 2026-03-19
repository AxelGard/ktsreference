

# atomicLazy

Error since 2.1

```kotlin
fun <T> atomicLazy(initializer: () -> T): Lazy<T>(source)
```

```kotlin
import kotlin.native.concurrent.atomicLazy

class Demo {
    // Lazily initialized property that is thread‑safe
    val expensiveValue: Int by atomicLazy {
        println("Computing value")
        42
    }

    fun printValue() {
        // The initializer runs only once, even if called from multiple threads
        println("Value: $expensiveValue")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native.concurrent/atomic-lazy.html)

    