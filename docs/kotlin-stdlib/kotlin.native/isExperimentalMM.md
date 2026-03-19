

# isExperimentalMM

This property always returns true, its usages can be safely removed.

```kotlin
@ExperimentalStdlibApifun isExperimentalMM(): Boolean(source)
```

```kotlin
import kotlin.native.isExperimentalMM

@OptIn(ExperimentalStdlibApi::class)
fun main() {
    if (isExperimentalMM) {
        println("Experimental MM is enabled.")
    } else {
        println("Experimental MM is disabled.")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/is-experimental-m-m.html)

    