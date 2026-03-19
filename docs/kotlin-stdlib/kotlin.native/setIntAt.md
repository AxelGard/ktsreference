

# setIntAt

Sets Int out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.setIntAt(index: Int, value: Int)(source)
```

```kotlin
import kotlin.native.ExperimentalNativeApi

@ExperimentalNativeApi
fun main() {
    val buffer = ByteArray(8)          // 8 bytes = 2 Ints
    buffer.setIntAt(0, 42)             // store 42 at bytes 0‑3
    buffer.setIntAt(4, 65536)          // store 65536 at bytes 4‑7
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/set-int-at.html)

    